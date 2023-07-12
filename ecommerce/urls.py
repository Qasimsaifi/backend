from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet , FileUploadViewSet

app_name = 'ecommerce'

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'files', FileUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
