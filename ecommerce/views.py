from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, ProductImage , FileUpload
from .serializers import ProductSerializer , FileUploadSerializer

class FileUploadViewSet(ReadOnlyModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags', 'slug', 'is_published']  # Add the desired filter fields
    search_fields = ['category__name', 'slug']  # Specify the search fields
    ordering_fields = ['date']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        image_urls = [image.image.url for image in instance.images.all()]
        response_data = serializer.data
        response_data['image_urls'] = image_urls

        return Response(response_data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        for item in serializer.data:
            product = Product.objects.get(pk=item['id'])
            image_urls = [image.image.url for image in product.images.all()]
            item['image_urls'] = image_urls

        return Response(serializer.data, status=status.HTTP_200_OK)
