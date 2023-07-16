from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Project, Contact, BlogPost
from .serializers import ProjectSerializer, ContactSerializer, BlogPostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Custom pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10  # Set the number of items to display per page
    page_size_query_param = 'page_size'  # Allow overriding the page size via query parameter
    max_page_size = 100  # Set the maximum allowed page size

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'slug']
    search_fields = ['title', 'slug']
    ordering_fields = ['created_at']
    pagination_class = CustomPagination  # Enable pagination

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags', 'slug', 'title', 'is_published']
    search_fields = ['category', 'slug']
    ordering_fields = ['created_at']
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination  # Enable pagination

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['is_contacted']
    pagination_class = CustomPagination  # Enable pagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
