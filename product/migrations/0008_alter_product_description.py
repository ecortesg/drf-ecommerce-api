# Generated by Django 4.2.2 on 2023-12-15 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_carouselimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]