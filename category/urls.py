from django.urls import path
from .views import CategoryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', CategoryView)

urlpatterns = [
    path('', CategoryView.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += router.urls
