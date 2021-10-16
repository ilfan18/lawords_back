from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator
)
from django.db import models
from .services import *


class AuthUser(models.Model):
    """Модель пользователя."""

    email = models.EmailField('эмейл', max_length=150, unique=True)
    join_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    level_choices = [
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
        null=True,
        blank=True,
    )
    display_name = models.CharField(
        'Имя', max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(
        'Возраст',
        null=True,
        blank=True,
        default=18,
        validators=[
            MaxValueValidator(limit_value=0, message='Недопустимое значение')
        ]
    )
    avatar = models.ImageField(
        'Аватар',
        upload_to=get_path_upload_avatar,
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png']),
            validate_size_image
        ]
    )

    @property
    def is_authenticated(self):
        """Всегда возвращает True, таким образом можно узнать, что пользователь аутентифицирован."""
        return True

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
