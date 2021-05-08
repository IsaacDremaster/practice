from django.contrib import admin
from django.urls import path, include

from user.views import ProfileRegisterView, ProfileLoginView, StuffRegisterView, StuffLoginView
from category.views import CategoryView
from product.views import Product
from product.views import ProductView

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/register', ProfileRegisterView.as_view()),
    path('profile/login', ProfileLoginView.as_view()),
    path('stuff/register', StuffRegisterView.as_view()),
    path('stuff/login', StuffLoginView.as_view()),
    path('categories/', include('category.urls')),
    path('products/', include('product.urls')),
    path('orders/', include('order.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)