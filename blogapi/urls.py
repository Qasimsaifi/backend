from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to BlogAxis API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('api/v1/blog', include('blogpost.urls')),
    path('api/v1/snippets/', include('snippets.urls')),
]
