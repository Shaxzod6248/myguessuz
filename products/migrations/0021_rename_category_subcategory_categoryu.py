# Generated by Django 4.2.11 on 2024-05-30 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_products_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='category',
            new_name='categoryu',
        ),
    ]
