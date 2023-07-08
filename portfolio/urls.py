from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSet , ContactViewSet , BlogPostViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'blog', BlogPostViewSet, basename='blogPosts')


urlpatterns = [
    path("", include(router.urls)),
]
