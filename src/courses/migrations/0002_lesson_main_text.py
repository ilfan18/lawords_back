# Generated by Django 3.2.8 on 2021-12-29 17:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='main_text',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]