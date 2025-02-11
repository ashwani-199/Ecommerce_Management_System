from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mysite_management.common_module.mainService import MainService

urlpatterns = [
    path('admin1/', admin.site.urls),
    # path('api/', include('apps.apis.urls')),
    path('admin/', include('apps.login.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('users/', include('apps.users.urls')),
    path('customers/', include('apps.customers.urls')),
    path('products/', include('apps.product.urls')),
    path('orders/', include('apps.orders.urls')),
    path('shipping-cart/', include('apps.shipping_cart.urls')),


    path('', include('fronts.home.urls')),
    path('', include('fronts.contact.urls')),


]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = MainService.error_404
handler500 = MainService.error_500
handler403 = MainService.error_403
handler400 = MainService.error_400
