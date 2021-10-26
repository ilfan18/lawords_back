from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator
)
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
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
    age = models.PositiveIntegerField(
        'Возраст',
        null=True,
        blank=True,
        default=18,
        validators=[
            MaxValueValidator(limit_value=100, message='Недопустимое значение')
        ]
    )

    def __str__(self):
        return f'Профиль {self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


# avatar = models.ImageField(
#     'Аватар',
#     upload_to=get_path_upload_avatar,
#     null=True,
#     blank=True,
#     validators=[
#         FileExtensionValidator(allowed_extensions=['jpg', 'png']),
#         validate_size_image
#     ]
# )

# @property
# def is_authenticated(self):
#     """Всегда возвращает True, таким образом можно узнать, что пользователь аутентифицирован."""
#     return True
