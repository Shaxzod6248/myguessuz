# Generated by Django 4.2.11 on 2024-05-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='Categoryimage'),
        ),
    ]
