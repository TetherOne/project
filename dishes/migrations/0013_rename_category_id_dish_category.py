# Generated by Django 5.0.4 on 2024-04-12 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dishes", "0012_rename_category_dishcategory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dish",
            old_name="category_id",
            new_name="category",
        ),
    ]
