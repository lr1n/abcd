from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.decorators.http import require_POST
from res_app.models import Food
from .cart import Cart
from .forms import CartAddFoodForm


@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddFoodForm()
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, food_id)
    cart.remove(food)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', context={'cart': cart})

