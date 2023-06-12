from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.text import slugify

class CodeSnippet(models.Model):
    PRIVACY_CHOICES = (
        (0, 'Public'),
        (1, 'Private'),
    )

    author = models.ForeignKey(User, to_field='username', default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255, default='', null=True)
    content = HTMLField()
    code_snippet = HTMLField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.IntegerField(choices=PRIVACY_CHOICES, default=0)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    snippet = models.ForeignKey(CodeSnippet, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
