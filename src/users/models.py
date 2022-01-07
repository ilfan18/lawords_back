from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import (
    MaxValueValidator
)
from django.contrib.auth.models import AbstractUser


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
        blank=True,
        through='UserLesson',
        through_fields=('user', 'lesson')
    )

    def __str__(self):
        return f'Профиль {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserLesson(models.Model):
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE,
    )
    lesson = models.ForeignKey(
        verbose_name='Урок',
        to='courses.Lesson',
        on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField(
        'Балл',
        default=0,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username + ' - ' + self.lesson.name

    class Meta:
        verbose_name = 'Урок пользователя'
        verbose_name_plural = 'Уроки пользователей'
