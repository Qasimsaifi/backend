from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100, default="Qasim Saifi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name