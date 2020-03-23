from rest_framework import serializers
from ..models import (Restaurant,
                      Food,)


class RestaurantSerializer(serializers.ModelSerializer):
    cuisine_name = serializers.SerializerMethodField()

    def get_cuisine_name(self, obj: Restaurant):
        return obj.get_cuisine_display()

    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    restaurant_obj = RestaurantSerializer(
        source='restaurant',
        read_only=True,
    )

    class Meta:
        model = Food
        fields = '__all__'


