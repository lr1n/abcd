from django.urls import path, include
from .views import (index,
                    RestaurantListView,
                    RestaurantCreateView,
                    RestaurantDetailView,
                    RestaurantUpdateView,
                    RestaurantDeleteView,
                    FoodListView,
                    FoodCreateView,
                    FoodDetailView,
                    FoodUpdateView,
                    FoodDeleteView,
                    create_restaurant,
                    IndexView)
app_name = 'res_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('restaurant_list/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant_create/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('restaurant_detail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurant_update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('restaurant_delete/<int:pk>/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
    path('api/', include('res_app.api.urls')),
    path('food_list/', FoodListView.as_view(), name='food_list'),
    path('food_create/', FoodCreateView.as_view(), name='food_create'),
    path('food_detail/<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('food_update/<int:pk>/', FoodUpdateView.as_view(), name='food_update'),
    path('food_delete/<int:pk>/', FoodDeleteView.as_view(), name='food_delete'),
    path('create_restaurant_with_func/', create_restaurant, name='create_restaurant_with_func')
]