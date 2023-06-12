from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CodeSnippet, Comment
from .serializers import CodeSnippetSerializer, CommentSerializer
import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

class CodeSnippetFilter(django_filters.FilterSet):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'title', 'author']

class CodeSnippetPagination(PageNumberPagination):
    page_size = 10

class CodeSnippetViewSet(viewsets.ModelViewSet):
    queryset = CodeSnippet.objects.all()
    serializer_class = CodeSnippetSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    filterset_class = CodeSnippetFilter
    ordering_fields = ['publication_date']
    pagination_class = CodeSnippetPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['snippet']

class CommentPagination(PageNumberPagination):
    page_size = 10

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    filterset_class = CommentFilter
    ordering_fields = ['created_at']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


