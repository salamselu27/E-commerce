from django.shortcuts import render, get_object_or_404
from . import models
from .models import Category, Product

def home(request):
    products = Product.objects.filter(available=True)
    sliders = models.Slider.objects.filter(active=True)
    
    # Dynamic Sections
    top_deals = products.filter(discount_price__isnull=False).order_by('?')[:10] # logic can be improved
    featured_products = products.filter(is_featured=True)[:8]
    top_selling = products.filter(is_bestseller=True)[:4] # Assuming 4 for the row or slider
    
    # Recommendation Logic
    recommended_products = Product.objects.none()
    if request.user.is_authenticated:
        # Simple recommendation: show products marked as recommended, or random if none
        recommended_products = products.filter(is_recommended=True)[:8]
        if not recommended_products.exists():
             recommended_products = products.order_by('?')[:8]
    
    context = {
        'products': products, # Default list if needed
        'sliders': sliders,
        'top_deals': top_deals,
        'featured_products': featured_products,
        'top_selling': top_selling,
        'recommended_products': recommended_products,
    }
    return render(request, 'shop/index.html', context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product_list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})
