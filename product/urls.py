from django.urls import path
from .views import ProductView

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', ProductView)

urlpatterns = [
    path('', ProductView.as_view({'get': 'list'})),
]
urlpatterns += router.urls