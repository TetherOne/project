# Generated by Django 5.0.4 on 2024-04-10 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_remove_dish_nutritional_value_dishinfo_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishinfo',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_info', to='dishes.dish'),
        ),
    ]