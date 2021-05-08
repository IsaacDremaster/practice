from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category
from .serializers import CategorySerializer
from .service import CategoryFilter
from .permissions import IsUserOwnerOrReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, Response


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsUserOwnerOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = CategoryFilter
