from django.test import TestCase, Client
from django.urls import reverse
from ..models import Restaurant, Food


class TestRestaurantViews(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='restaurant',
            cuisine='2',
            address='some adr',
            work_from='09:00',
            work_to='21:00'
        )
        self.client = Client()
        self.restaurant_create = reverse('res_app:restaurant_create')
        self.restaurant_list = reverse('res_app:restaurant_list')
        self.restaurant_detail = reverse('res_app:restaurant_detail', args=['1'])
        self.restaurant_delete = reverse('res_app:restaurant_delete', args=['1'])
        self.restaurant_update = reverse('res_app:restaurant_update', args=['1'])

    def test_restaurant_create(self):
        response = self.client.get(self.restaurant_create)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/restaurant_create.html')

    def test_restaurant_list(self):
        response = self.client.get(self.restaurant_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed((response, 'res_app/restaurant_list.html'))

    def test_restaurant_detail(self):
        response = self.client.get(self.restaurant_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/restaurant_detail.html')

    def test_restaurant_delete(self):
        response = self.client.get(self.restaurant_delete)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/restaurant_delete.html')

    def test_restaurant_update(self):
        response = self.client.get(self.restaurant_update)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/restaurant_create.html')


class TestFoodViews(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='rest',
            cuisine='1',
            address='address',
            work_from='10:00',
            work_to='22:00'
        )
        self.food = Food.objects.create(
            name='some food',
            type_of_food='1',
            restaurant=self.restaurant,
            price='10',
            sauce='1'
        )
        self.client = Client()
        self.index = reverse('res_app:index')
        self.food_create = reverse('res_app:food_create')
        self.food_list = reverse('res_app:food_list')
        self.food_detail = reverse('res_app:food_detail', args=['1'])
        self.food_delete = reverse('res_app:food_delete', args=['1'])
        self.food_update = reverse('res_app:food_update', args=['1'])

    def test_index(self):
        response = self.client.get(self.index)
        self.assertEqual(response.status_code, 302)

    def test_food_create(self):
        response = self.client.get(self.food_create)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/food_create.html')

    def test_food_list(self):
        response = self.client.get(self.food_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/food_list.html')

    def test_food_detail(self):
        response = self.client.get(self.food_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/food_detail.html')

    def test_food_delete(self):
        response = self.client.get(self.food_delete)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/food_delete.html')

    def test_food_update(self):
        response = self.client.get(self.food_update)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'res_app/food_create.html')


