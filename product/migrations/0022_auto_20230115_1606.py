# Generated by Django 3.2.8 on 2023-01-15 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_order_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='menu_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top_menu_name', to='product.topmenu'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_menu_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.submenu'),
        ),
    ]
