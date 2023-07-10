# Generated by Django 3.2.8 on 2022-06-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_couponcodeusage_coupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=130, null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(max_length=300)),
                ('appartment_no', models.CharField(max_length=130)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(default='INDIA', max_length=100)),
                ('zip_code', models.CharField(max_length=30)),
                ('coupon_code', models.CharField(blank=True, max_length=200, null=True)),
                ('discount', models.CharField(blank=True, max_length=200, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=200, null=True)),
                ('bill', models.TextField(max_length=130, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=200, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('privacy_policy', models.BooleanField(default=True)),
            ],
        ),
    ]
