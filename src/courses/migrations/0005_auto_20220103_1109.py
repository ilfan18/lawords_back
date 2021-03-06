# Generated by Django 3.2.8 on 2022-01-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_exercise_exercise_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(blank=True, help_text='Оставьте пустым, если тип не "Перевод с картинки"', null=True, upload_to='lessons/icons/', verbose_name='Картинка к заданию'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='text',
            field=models.TextField(help_text='Используйте "__" для пропуска', max_length=500, verbose_name='Текст вопроса'),
        ),
    ]
