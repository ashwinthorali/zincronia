# Generated by Django 3.2.8 on 2022-06-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=900)),
                ('keyword', models.CharField(max_length=156)),
                ('title', models.CharField(max_length=156)),
                ('og_type', models.CharField(max_length=156)),
                ('og_card', models.CharField(max_length=156)),
                ('image', models.ImageField(upload_to='SEO')),
            ],
        ),
    ]
