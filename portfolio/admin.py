from django.contrib import admin
from .models import Project

@admin.register(Project)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id", "title","link"]

# Register your models here.
