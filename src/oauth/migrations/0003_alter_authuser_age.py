# Generated by Django 3.2.8 on 2021-10-16 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20211016_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=18, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=0, message='Недопустимое значение')], verbose_name='Возраст'),
        ),
    ]
