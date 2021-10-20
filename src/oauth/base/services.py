from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file) -> str:
    """Построение пути к файлу аватара, format: (media)/avatars/user_id/photo.jpg"""

    return f'avatars/{instance.id}/{file}'


def validate_size_image(file_obj):
    """Проверка размера файла"""

    megabite_limit = 2

    if file_obj.size > megabite_limit*1024*1024:
        raise ValidationError(f'Максимальный размер файла {megabite_limit}')
