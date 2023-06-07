from django.db import models
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    publication_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')])

    def __str__(self):
        return self.title

