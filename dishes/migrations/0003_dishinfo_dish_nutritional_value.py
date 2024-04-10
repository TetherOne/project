# Generated by Django 5.0.4 on 2024-04-10 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_alter_dish_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('proteins', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('fats', models.FloatField()),
                ('kilocalories_per_100_grams', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='nutritional_value',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='dishes.dishinfo'),
            preserve_default=False,
        ),
    ]
