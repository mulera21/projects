from django.shortcuts import render, get_object_or_404
from store.models import Products
from store .models import Category, Products, Order,Customer


#  products
def all_products(request):
    products = Products.objects.all()
    return render(request, 'store/product.html', {'products': products})

#product by category
def products_by_category(request, category_id):
    products = Products.objects.filter(category=category_id)
    return render(request, 'products.html', {'products': products})

#order placing
def place_order(request, product_id):
    if request.method == 'POST':
        # Assuming form data is submitted with product quantity, customer info, etc.
        product = Products.objects.get(pk=product_id)
        customer = Customer.objects.get(pk=request.POST.get('customer_id'))  # Assuming customer_id is submitted in the form
        quantity = request.POST.get('quantity')
        price = product.price * int(quantity)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        new_order = Order(product=product, customer=customer, quantity=quantity, price=price, address=address, phone=phone)
        new_order.placeOrder()
        return render(request, 'order_placed.html')
    else:
        # Retrieve product details for order placement form
        product = Products.objects.get(pk=product_id)
        return render(request, 'place_order.html', {'product': product})




