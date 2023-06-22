from django.urls import path, include
from rest_framework import routers
from .views import UserDetailView, PublicUserViewSet

router = routers.DefaultRouter()
router.register('publicuser', PublicUserViewSet, basename='public-user')

urlpatterns = [
    # other paths
    path('', UserDetailView.as_view(), name='user-detail'),
    path('public/', include(router.urls)),
]
