from django.urls import path, include
from rest_framework import routers
from .views import UserDetailView, PublicUserViewSet, ForgotPasswordView , ResetPasswordView

router = routers.DefaultRouter()
router.register('publicuser', PublicUserViewSet, basename='public-user')

urlpatterns = [
    # Other URL patterns
    
    # Endpoint for user detail view
    path('', UserDetailView.as_view(), name='user-detail'),
    
    # Endpoint for public user viewset
    path('public/', include(router.urls)),
    
    # Endpoint for forgot password view
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset_password'),
]
