# Generated by Django 3.2.8 on 2022-06-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220611_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='note',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
    ]
