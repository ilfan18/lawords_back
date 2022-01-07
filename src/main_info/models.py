from django.db import models


class BaseSiteInfo(models.Model):
    """Основные настройки сайта"""
    image = models.ImageField(
        'Логотип',
        upload_to='logo',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Профиль {self.username}'

    class Meta:
        verbose_name = 'Основная настройки'
        verbose_name_plural = 'Основные настройки'
