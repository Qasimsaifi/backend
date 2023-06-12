from rest_framework import viewsets, permissions, generics
from django.db import models
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CodeSnippet, Comment
from .serializers import CodeSnippetSerializer, CommentSerializer
import django_filters.rest_framework

class CodeSnippetFilter(django_filters.FilterSet):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'title', 'author' , 'slug']

class CodeSnippetPagination(PageNumberPagination):
    page_size = 10

class IsTokenAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        token_author = request.user.username
        return obj.author.username == token_author

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

class CodeSnippetViewSet(viewsets.ModelViewSet):
    queryset = CodeSnippet.objects.all()
    serializer_class = CodeSnippetSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    filterset_class = CodeSnippetFilter
    ordering_fields = ['publication_date']
    pagination_class = CodeSnippetPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTokenAuthorOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(
                models.Q(is_private=False) |
                models.Q(is_private=True, author=self.request.user)
            )
        else:
            return queryset.filter(is_private=False)


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

class ModelAuthView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Implement your custom logic here
        # Return the desired response
        pass
