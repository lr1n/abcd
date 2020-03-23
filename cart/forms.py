from django import forms


FOOD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddFoodForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=FOOD_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)