from django.urls import path
from . import views

app_name='shopping'

urlpatterns  = [
    path('',views.Index, name='index'),
    path('allproduct/',views.allProduct, name='allproduct'),
    path('editproduct/<int:product_pk>',views.editProduct, name='editproduct'),
    path('addproduct/',views.addProduct, name='addproduct'),
    path('editproduct/<int:product_pk>/deleteproduct', views.deleteProduct, name='deleteproduct'),

]