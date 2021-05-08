from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView, Response

from .models import Product
from .serializers import ProductSerializer
from .service import ProductFilter
from .permissions import IsProductUserOrReadOnly


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsProductUserOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = ProductFilter
