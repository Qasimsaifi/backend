from django.urls import path
from .views import UserDetailView

urlpatterns = [
    # other paths
    path('', UserDetailView.as_view(), name='user-detail'),
]
