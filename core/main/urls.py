from django.urls import path
from . import views
from .views import  HomeListView, ErorListView, CheckoutListView, FooterListView, ShopListView, ProductListView, BlogListView, BlogSingleListView, CartListView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('404/', ErorListView.as_view(), name='eror'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
    path('product_detail/', ProductListView.as_view(), name='product'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_single/', BlogSingleListView.as_view(), name='blog_single'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('', FooterListView.as_view(), name='footer')
    
    
]