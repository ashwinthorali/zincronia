# Generated by Django 3.2.8 on 2022-06-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_products_sold_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='new_arrival',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
