# Generated by Django 3.2.8 on 2021-10-26 17:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=18, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=100, message='Недопустимое значение')], verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('elementary', 'Elementary'), ('intermediate', 'Intermediate'), ('upper_intermediate', 'Upper-Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=500, null=True, verbose_name='Уровень'),
        ),
    ]
