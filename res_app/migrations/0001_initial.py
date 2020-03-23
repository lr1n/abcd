# Generated by Django 3.0.4 on 2020-03-18 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(choices=[('1', 'Fast food'), ('2', 'Asian'), ('3', 'Italian')], max_length=200, verbose_name='Cuisine')),
                ('name', models.CharField(max_length=250, verbose_name='Name of restaurant')),
                ('address', models.CharField(max_length=200, verbose_name='Address of restaurant')),
                ('work_from', models.TimeField()),
                ('work_to', models.TimeField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=None, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name of food')),
                ('type_of_food', models.CharField(choices=[('1', 'Salads'), ('2', 'Sandwiches'), ('3', 'Soups'), ('4', 'Main Coursers'), ('5', 'Desserts'), ('6', 'Drinks')], max_length=300, verbose_name='Menu')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('sauce', models.CharField(choices=[('1', 'Mayonnaise'), ('2', 'Ketchup'), ('3', 'Soy sauce'), ('4', 'BBQ sauce'), ('5', 'Mustard'), ('6', 'Garlic sauce')], max_length=200, verbose_name='Sauce')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='res_app.Restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
            },
        ),
    ]