# Generated by Django 4.0.4 on 2022-06-17 08:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_mostpopularblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
