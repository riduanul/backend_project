from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from django.core.cache import cache
from rest_framework.response import Response
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #Only authenticated and admin user can access create/update/delete api and user only can get the product   
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    #caching for the list action (GET request)
    def list(self, request, *args, **kwargs):
        cache_key = 'product_list'
        cache_data = cache.get(cache_key)

        if cache_data is None:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            cache_data = serializer.data
            cache.set(cache_key, cache_data, timeout= 60 * 30) # 30 minutes
        
        return Response(cache_data)