from django import forms
from .models import (Restaurant, Food)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Save restaurant')
        )


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
