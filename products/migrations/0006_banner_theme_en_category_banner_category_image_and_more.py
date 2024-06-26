# Generated by Django 4.2.11 on 2024-05-21 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='theme_en',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.banner'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='categoryimg'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='title_en',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(null=True, upload_to='Bannerpic'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='theme_ru',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='theme_uz',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='name_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='products_image'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='title_ru',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='title_uz',
            field=models.CharField(max_length=20000, null=True),
        ),
    ]
