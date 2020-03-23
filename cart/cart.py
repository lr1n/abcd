from decimal import Decimal
from django.conf import settings
from res_app.models import Food


class Cart(object):  # initialize cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, food, quantity=1, update_quantity=False):  # add food in cart or update quantity
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity': 0,
                                  'price': str(food.price)}
        if update_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart  # update cart session
        self.session.modified = True  # notice like 'modified'

    def remove(self, food):  # remove from cart
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()

    def __iter__(self):
        food_ids = self.cart.keys()
        foods = Food.objects.filter(id__in=food_ids)
        for food in foods:
            self.cart[str(food.id)]['food'] = food

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
