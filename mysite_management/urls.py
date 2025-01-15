from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('apps.apis.urls')),
    path('admin1/', include('apps.login.urls')),
    path('', include('apps.dashboard.urls')),
    path('users/', include('apps.users.urls')),
    path('customers/', include('apps.customers.urls')),
    path('products/', include('apps.product.urls')),
    path('orders/', include('apps.orders.urls')),
    path('shipping-cart/', include('apps.shipping_cart.urls')),


    path('', include('fronts.home.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
