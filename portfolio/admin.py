from django.contrib import admin
from .models import Project, Contact, BlogPost, Category, Tag


@admin.register(Project)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "link"]


@admin.register(Contact)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "message"]


@admin.register(BlogPost)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category"]


@admin.register(Category)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Tag)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id"]


# Register your models here.
