from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSet , ContactViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contacts', ContactViewSet, basename='contact')


urlpatterns = [
    path("", include(router.urls)),
]
