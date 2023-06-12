from django.contrib import admin
from .models import CodeSnippet
from .models import Comment


@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","snippet", "content"]
