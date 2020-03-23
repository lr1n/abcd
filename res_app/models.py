from django.db import models
from PIL import Image
from django.urls import reverse


class Restaurant(models.Model):
    CUISINE = (
        ('1', 'Fast food'),
        ('2', 'Asian'),
        ('3', 'Italian')
    )

    cuisine = models.CharField(
        max_length=200,
        choices=CUISINE,
        verbose_name='Cuisine',
    )

    name = models.CharField(
        max_length=250,
        verbose_name='Name of restaurant'
    )

    address = models.CharField(
        max_length=200,
        verbose_name='Address of restaurant'
    )

    work_from = models.TimeField()
    work_to = models.TimeField()

    image = models.ImageField(
        upload_to='image/res_app/%Y/%m/%d',
        default=None,
        blank=True,
        null=True,
        verbose_name='Image'
    )

    def save(self, *args, **kwargs):
        try:
            this_entry = Restaurant.objects.get(id=self.id)
            if this_entry.image != self.image:
                this_entry.image.delete(save=False)
        except:
            pass
        super(Restaurant, self).save(*args, **kwargs)
        print(self.image)
        if self.image:
            image = Image.open(self.image.path)
            max_size = max(image.size[0], image.size[1])
            multiplier = max_size / 1200
            image = image.resize((round(image.size[0] / multiplier), round(image.size[1] / multiplier)), Image.ANTIALIAS)
            image.save(self.image.path)
            print(image.size)

            image.save(self.image.path)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Restaurant, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('res_app:restaurant_update', args=(self.id,))

    def __str__(self):
        return f'{self.name} {self.get_cuisine_display()} {self.address} {self.work_from} {self.work_to}'

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class Food(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Name of food'
    )

    TYPE_OF_FOOD = (
        ('1', 'Salads'),
        ('2', 'Sandwiches'),
        ('3', 'Soups'),
        ('4', 'Main Dishes'),
        ('5', 'Desserts'),
        ('6', 'Drinks')
    )

    type_of_food = models.CharField(
        choices=TYPE_OF_FOOD,
        max_length=300,
        verbose_name='Menu',
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.DO_NOTHING,
        verbose_name='Restaurant'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price',
    )

    SAUCE = (
        ('1', 'Mayonnaise'),
        ('2', 'Ketchup'),
        ('3', 'Soy sauce'),
        ('4', 'BBQ sauce'),
        ('5', 'Mustard'),
        ('6', 'Garlic sauce')
    )

    sauce = models.CharField(
        choices=SAUCE,
        max_length=200,
        verbose_name='Sauce'
    )

    image = models.ImageField(
        upload_to='image/res_app/%Y/%m/%d',
        default=None,
        blank=True,
        null=True,
        verbose_name='Image'
    )

    def save(self, *args, **kwargs):
        try:
            this_entry = Food.objects.get(id=self.id)
            if this_entry.image != self.image:
                this_entry.image.delete(save=False)
        except:
            pass
        super(Food, self).save(*args, **kwargs)
        print(self.image)
        if self.image:
            image = Image.open(self.image.path)
            max_size = max(image.size[0], image.size[1])
            multiplier = max_size / 1200
            image = image.resize((round(image.size[0] / multiplier), round(image.size[1] / multiplier)),
                                 Image.ANTIALIAS)
            image.save(self.image.path)
            print(image.size)

            image.save(self.image.path)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Food, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('res_app:food_update', args=(self.id,))

    def __str__(self):
        return f'{self.name} {self.restaurant} {self.get_type_of_food_display()}' \
               f' {self.get_sauce_display()} {self.price}'

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'










