from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.http import JsonResponse
from foodmain.models import Food

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        food_id = int(request.POST.get('food_id'))
        food = get_object_or_404(Food, id=food_id)
        cart.add(food=food)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass