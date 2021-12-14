from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator
)
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# class Profile(models.Model):
#     user = models.OneToOneField(
#         verbose_name='Пользователь',
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='profile',
#     )
#     image = models.ImageField(
#         'Аватар',
#         upload_to='profile_pics',
#         default='default.jpg',
#         null=True,
#         blank=True,
#     )
#     level_choices = [
#         ('', 'Выберите уровень'),
#         ('beginner', 'Beginner'),
#         ('elementary', 'Elementary'),
#         ('intermediate', 'Intermediate'),
#         ('upper_intermediate', 'Upper-Intermediate'),
#         ('advanced', 'Advanced'),
#     ]
#     level = models.CharField(
#         'Уровень',
#         max_length=500,
#         choices=level_choices,
#         default='beginner',
#         blank=True,
#     )
#     age = models.PositiveIntegerField(
#         'Возраст',
#         default=18,
#         null=True,
#         blank=True,
#         validators=[
#             MaxValueValidator(limit_value=100, message='Недопустимое значение')
#         ]
#     )
#     courses = models.ManyToManyField(
#         verbose_name='Выполненные курсы',
#         to='courses.Course',
#         related_name='users',
#         blank=True
#     )
#     lessons = models.ManyToManyField(
#         verbose_name='Выполненные уроки',
#         to='courses.Lesson',
#         related_name='users',
#         blank=True
#     )

#     def __str__(self):
#         return f'Профиль {self.user.username}'

#     class Meta:
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Профили'


class User(AbstractUser):
    image = models.ImageField(
        'Аватар',
        upload_to='profile_pics',
        default='default.jpg',
        null=True,
        blank=True,
    )
    level_choices = [
        ('', 'Выберите уровень'),
        ('beginner', 'Beginner'),
        ('elementary', 'Elementary'),
        ('intermediate', 'Intermediate'),
        ('upper_intermediate', 'Upper-Intermediate'),
        ('advanced', 'Advanced'),
    ]
    level = models.CharField(
        'Уровень',
        max_length=500,
        choices=level_choices,
        default='beginner',
        blank=True,
    )
    age = models.PositiveIntegerField(
        'Возраст',
        default=18,
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(limit_value=100, message='Недопустимое значение')
        ]
    )
    courses = models.ManyToManyField(
        verbose_name='Выполненные курсы',
        to='courses.Course',
        related_name='users',
        blank=True
    )
    lessons = models.ManyToManyField(
        verbose_name='Выполненные уроки',
        to='courses.Lesson',
        related_name='users',
        blank=True
    )

    def __str__(self):
        return f'Профиль {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
