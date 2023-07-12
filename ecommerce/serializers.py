from rest_framework import serializers
from .models import Product , FileUpload

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('images',)


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'