# Generated by Django 3.2.8 on 2023-01-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20230115_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='spec',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
