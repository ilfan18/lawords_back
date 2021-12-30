# Generated by Django 3.2.8 on 2021-12-29 18:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson_main_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='top_text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Верхний текст'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='main_text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Основной текст'),
        ),
    ]