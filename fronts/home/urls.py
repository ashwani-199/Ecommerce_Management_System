from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home.index'),
    path('about/', views.about, name='home.about'),
    path('product-items/', views.product, name='home.products_item'),
    path('product-details/<int:id>/', views.productDetails, name='home.product_details'),
    path('shopping-cart/', views.shopCart, name='home.shopping_cart'),
    path('contacts/', views.contacts, name='home.contacts'),
    path('category/<str:foo>/', views.category, name='home.category'),


    path('login/', views.login_user, name='home.login_user'),
    path('register/', views.register_user, name='home.register_user'),
    path('logout/', views.user_logout, name='home.logout_user'),

    path('review/', views.product_review, name='home.review'),
]