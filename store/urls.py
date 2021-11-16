from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name="index"),
    path('store/<slug:category_name>/', views.category, name="category"),
    path('store/<slug:category_name>/<slug:subcategory_name>', views.subcategory, name="subcategory"), 
    path('services/', views.service, name="service"),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name="contact"),
]