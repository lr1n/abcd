from django.http import (HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseNotAllowed)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.urls import (reverse, reverse_lazy)
from django.template.response import TemplateResponse
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView,
                                  View,
                                  TemplateView)
from .models import (Restaurant, Food )
from .forms import (RestaurantForm,
                    FoodForm,
                    )
from cart.forms import CartAddFoodForm


# def food_detail(request, id):
#     food = get_object_or_404(Food,
#                              id=id,
#                              available=True)
#     cart_food_form = CartAddFoodForm()
#     return render(request, 'res_app/food_detail.html', context={'food': food,
#                                                                 'cart_food_form': cart_food_form})


def index(request):
    return render(request, 'res_app/base.html', context={})


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users_app:login')
    template_name = 'res_app/base.html'


class RestaurantListView(ListView):
    template_name = 'res_app/restaurant_list.html'
    model = Restaurant
    context_object_name = 'restaurant_list'
    paginate_by = 2

    def get_queryset(self):
        # return Restaurant.objects.select_related()
        return Restaurant.objects.all()

    def get_paginate_by(self, queryset):
        page_number = self.request.GET.get('page_number')
        if page_number is not None:
            self.paginate_by = page_number
        return super(RestaurantListView, self).get_paginate_by(
            self.get_queryset()
        )

    def get(self, request, *args, **kwargs):
        return super(RestaurantListView, self).get(request, *args, **kwargs)


def create_restaurant(request):
    if request.method == 'GET':
        restaurant_form = RestaurantForm()
        return render(request, 'res_app/create_restaurant_with_func.html',
                      context={'restaurant_form': restaurant_form})
    elif request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST)
        if restaurant_form.is_valid():
            restaurant_form.save(commit=True)
            return HttpResponseRedirect(reverse('res_app:restaurant_list'))
        else:
            return render(request, 'res_app/create_restaurant_with_func.html',
                          context={'restaurant_form': restaurant_form,
                                   'message': 'Wrong data in form!'})


class RestaurantCreateView(CreateView):
    model = Restaurant
    template_name = 'res_app/restaurant_create.html'
    form_class = RestaurantForm


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'res_app/restaurant_detail.html'
    context_object_name = 'restaurant'

    def get_queryset(self):
        return Restaurant.objects.all()


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    template_name = 'res_app/restaurant_create.html'
    form_class = RestaurantForm


class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('res_app:restaurant_list')
    template_name = 'res_app/restaurant_delete.html'


class FoodListView(ListView):
    template_name = 'res_app/food_list.html'
    model = Food
    context_object_name = 'food_list'
    paginate_by = 2

    def get_queryset(self):
        # return Restaurant.objects.select_related()
        return Food.objects.all()

    def get_paginate_by(self, queryset):
        page_number = self.request.GET.get('page_number')
        if page_number is not None:
            self.paginate_by = page_number
        return super(FoodListView, self).get_paginate_by(
            self.get_queryset()
        )

    def get(self, request, *args, **kwargs):
        return super(FoodListView, self).get(request, *args, **kwargs)


class FoodCreateView(CreateView):
    model = Food
    template_name = 'res_app/food_create.html'
    form_class = FoodForm


class FoodDetailView(DetailView):
    model = Food
    template_name = 'res_app/food_detail.html'
    context_object_name = 'food'

    def get_queryset(self):
        return Food.objects.all()


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'res_app/food_create.html'
    form_class = FoodForm


class FoodDeleteView(DeleteView):
    model = Food
    success_url = reverse_lazy('res_app:food_list')
    template_name = 'res_app/food_delete.html'





