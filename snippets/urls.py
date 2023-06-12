from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView, TokenVerifyView

router = routers.DefaultRouter()
router.register('snippet', views.CodeSnippetViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
    # ...
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name="Token_Get"),
    path('tokenrefresh/', TokenRefreshSlidingView.as_view(), name="Token_refresh"),
    path('tokenverify/', TokenVerifyView.as_view(), name="Token_verify"),
    path('tinymce/', include('tinymce.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework_api')),
]
