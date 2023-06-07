from django.contrib import admin
from .models import BlogPost, Category, Tag

admin.site.register(Category)
admin.site.register(Tag)

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content', 'author','category', 'likes', 'views', 'status']

