from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='orders.index'),
   path('edit/<int:id>/', views.edit, name='orders.edit'),
#    path('add-category/', views.addCategory, name='product.add_category'),
#    path('edit/<int:id>/', views.edit, name='product.edit'),
#    path('view/<int:id>/', views.view, name='product.view'),
#    path('delete/<int:id>/', views.delete, name='product.delete'),
   
]