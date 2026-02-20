from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Static pages
    path('about/', TemplateView.as_view(template_name='shop/about.html'), name='about'),
    path('blog/', TemplateView.as_view(template_name='shop/blog.html'), name='blog'),
    path('blog-details/', TemplateView.as_view(template_name='shop/blog-details.html'), name='blog_details'),
    path('cart/', TemplateView.as_view(template_name='shop/cart.html'), name='cart'),
    path('checkout/', TemplateView.as_view(template_name='shop/checkout.html'), name='checkout'),
    path('contact/', TemplateView.as_view(template_name='shop/contact.html'), name='contact'),
    path('faq/', TemplateView.as_view(template_name='shop/faq.html'), name='faq'),
    path('home-2/', TemplateView.as_view(template_name='shop/index-2.html'), name='home_2'),
    path('home-3/', TemplateView.as_view(template_name='shop/index-3.html'), name='home_3'),
    path('login/', TemplateView.as_view(template_name='shop/login.html'), name='login'),
    path('my-account/', TemplateView.as_view(template_name='shop/my-account.html'), name='my_account'),
    path('product-details-static/', TemplateView.as_view(template_name='shop/product-details.html'), name='product_details_static'),
    path('product-static/', TemplateView.as_view(template_name='shop/product.html'), name='product_static'),
    path('shop-details/', TemplateView.as_view(template_name='shop/shop-details.html'), name='shop_details'),
    path('shop-static/', TemplateView.as_view(template_name='shop/shop.html'), name='shop_static'),
    path('wishlist/', TemplateView.as_view(template_name='shop/wishlist.html'), name='wishlist'),
    path('404/', TemplateView.as_view(template_name='shop/404.html'), name='404'),
]
