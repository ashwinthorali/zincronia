# Generated by Django 3.2.8 on 2022-06-24 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_order_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
