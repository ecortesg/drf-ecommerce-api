# Generated by Django 4.2.2 on 2023-07-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_street_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_session_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
