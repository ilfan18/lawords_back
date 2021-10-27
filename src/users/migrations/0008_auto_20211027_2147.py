# Generated by Django 3.2.8 on 2021-10-27 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0007_auto_20211027_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(blank=True, choices=[('', 'Выберите уровень'), ('beginner', 'Beginner'), ('elementary', 'Elementary'), ('intermediate', 'Intermediate'), ('upper_intermediate', 'Upper-Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=500, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
