from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=100)
    description = HTMLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_digital = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    images = models.ManyToManyField("ProductImage", related_name="product_images", blank=True)
    cover_image = models.IntegerField(default=0 )
    payment_link = models.CharField(null=True , blank=True , max_length=200)
    file = models.URLField(null=True , blank=True)
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} - {self.product.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    image = CloudinaryField(blank=True, null=True)

    def __str__(self):
        return f"Image #{self.pk} - {self.image}"


class FileUpload(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    file = CloudinaryField(blank=True, null=True)

    def __str__(self):
        if self.file and self.file:
            return f"File #{self.pk} - {self.file}"
        return f"File #{self.pk} (No file uploaded)"

    def clean(self):
        if self.product.is_digital and not self.file:
            raise ValidationError("File is required for digital products.")
        elif not self.product.is_digital and self.file:
            raise ValidationError("File should not be provided for non-digital products.")
