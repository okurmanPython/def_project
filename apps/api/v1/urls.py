from django.urls import path, include

urlpatterns = [
    # path('account/', include('apps.account.urls')),
    path('products/', include('apps.product.urls')),
]