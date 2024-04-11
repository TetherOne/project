# Generated by Django 5.0.4 on 2024-04-10 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_dishinfo_dish_nutritional_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='nutritional_value',
        ),
        migrations.AddField(
            model_name='dishinfo',
            name='dish',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='dishes.dish'),
            preserve_default=False,
        ),
    ]