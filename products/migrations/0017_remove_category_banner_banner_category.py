# Generated by Django 4.2.11 on 2024-05-26 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_category_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='banner',
        ),
        migrations.AddField(
            model_name='banner',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
