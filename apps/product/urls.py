from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import ProductViewSet, ProductView

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('list/', ProductView.as_view(), name='product-list'),
    path('<int:pk>/detail/', ProductView.as_view(), name='product-detail'),
    path('', include(router.urls)),
]
