# Generated by Django 3.2.8 on 2023-02-18 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_auto_20230201_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.CharField(max_length=150)),
                ('comment', models.TextField()),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product_name', to='product.products')),
            ],
        ),
    ]