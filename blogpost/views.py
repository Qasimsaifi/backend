from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer
import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

class BlogPostFilter(django_filters.FilterSet):
    class Meta:
        model = BlogPost
        fields = ['id', 'slug', 'title', 'tags', 'author', 'category', 'status']

class BlogPostPagination(PageNumberPagination):
    page_size = 6

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('publication_date')
    serializer_class = BlogPostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    filterset_class = BlogPostFilter
    ordering_fields = ['publication_date']
    pagination_class = BlogPostPagination

