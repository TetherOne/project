# Generated by Django 5.0.4 on 2024-04-11 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_cart_user_alter_cart_dish"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="user",
            new_name="profile",
        ),
    ]
