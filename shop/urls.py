from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Commoncode/', views.Commoncode),
    path('Cart/', views.Cart, name='Cart'),
    path('Product_detail/', views.Product_detail, name='Product_detail'),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('Product/', views.Product, name='Product'),
    path('Product_two/', views.Product_two, name='Product_two'),
    path('Product_three/', views.Product_three, name='Product_three'),
    path('Contact/', views.Contact, name='Contact'),
    path('Errors/', views.Errors, name='Errors'),
    path('Blog_detail/', views.Blog_detail, name='Blog_detail'),
    path('Tracking/', views.Tracking, name='Tracking'),
    path('Profiles/', views.Profiles, name='Profiles'),
    path('login/', views.login, name='login'),
    path('Register/', views.Register, name='Register'),
    path('Forget_password/', views.Forget_password, name='Forget_password'),
]
