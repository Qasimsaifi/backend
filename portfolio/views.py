from rest_framework import viewsets, filters
from .models import Project
from .serializers import ProjectSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'slug']
    search_fields = ['title', 'slug']
    ordering_fields = ['created_at']
