from django.test import TestCase
from django.contrib.auth.models import User
from res_app.models import Restaurant, Food


class RestaurantTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant()
        self.restaurant.cuisine = '1'
        self.restaurant.name = 'some name'
        self.restaurant.address = 'some address'
        self.restaurant.work_from = '10:00'
        self.restaurant.work_to = '21:00'
        self.restaurant.save()

    def test_get_absolute_url_restaurant(self):
        self.assertEqual(self.restaurant.get_absolute_url(), '/restaurant_update/1/')


class FoodTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant()
        self.restaurant.cuisine = '1'
        self.restaurant.name = 'some name'
        self.restaurant.address = 'some address'
        self.restaurant.work_from = '10:00'
        self.restaurant.work_to = '21:00'
        self.restaurant.save()

        self.food = Food()
        self.food.name = 'some food name'
        self.food.type_of_food = '2'
        self.food.restaurant = self.restaurant
        self.food.price = '23'
        self.food.sauce = '3'
        self.food.save()

    def test_get_absolute_url_food(self):
        self.assertEqual(self.food.get_absolute_url(), '/food_update/1/')

    def test_food_name(self):
        self.assertEqual(self.food.name, 'some food name')


