# Generated by Django 4.2.11 on 2024-05-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_category_banner_banner_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotogallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Fotogalleryimg')),
            ],
        ),
    ]