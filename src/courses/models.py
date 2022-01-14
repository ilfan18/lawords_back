from django.db import models
from ckeditor.fields import RichTextField


class Course(models.Model):
    """Модель курса."""

    name = models.CharField('Название курса', max_length=255)
    level_choices = [
        ('', 'Выберите уровень курса'),
        ('beginner', 'Beginner'),
        ('elementary', 'Elementary'),
        ('intermediate', 'Intermediate'),
        ('upper_intermediate', 'Upper-Intermediate'),
        ('advanced', 'Advanced'),
    ]
    level = models.CharField(
        'Уровень курса',
        max_length=255,
        choices=level_choices,
        default='beginner',
        blank=True
    )
    new_words = models.PositiveIntegerField(
        'Число новых слов',
        default=0,
        blank=True
    )
    icon = models.ImageField(
        'Иконка курса',
        upload_to='courses/icons/',
        null=True,
        blank=True
    )
    cover = models.ImageField(
        'Обложка курса',
        upload_to='courses/covers/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = '   Курсы'
        ordering = ('pk',)


class Lesson(models.Model):
    """Модель урока."""

    name = models.CharField('Название урока', max_length=255)

    course = models.ForeignKey(
        verbose_name='Урок из курса',
        to='Course',
        on_delete=models.CASCADE,
        related_name='lessons',
        null=True,
        blank=True,
    )

    top_text = RichTextField(
        'Верхний текст',
        blank=True
    )

    main_text = RichTextField(
        'Основной текст',
        blank=True
    )

    icon = models.ImageField(
        'Иконка урока',
        upload_to='lessons/icons/',
        null=True,
        blank=True
    )
    cover = models.ImageField(
        'Обложка урока',
        upload_to='lessons/covers/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = '  Уроки'
        ordering = ('pk',)


class Exercise(models.Model):
    """Модель упражнения."""

    title = models.CharField('Название задания', max_length=255)
    lesson = models.ForeignKey(
        verbose_name='Задание из урока',
        to='Lesson',
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    type_choices = [
        ('', 'Выберите тип задания'),
        ('word_miss_type', 'Заполнить пропуск'),
        ('translate_type', 'Перевод с картинки'),
    ]
    exercise_type = models.CharField(
        'Тип задания',
        max_length=255,
        choices=type_choices,
        default='word_miss_type',
        blank=True
    )
    image = models.ImageField(
        'Картинка к заданию',
        upload_to='lessons/icons/',
        null=True,
        blank=True,
        help_text='Оставьте пустым, если тип не "Перевод с картинки"'
    )
    text = RichTextField(
        'Текст вопроса',
        help_text='Используйте "__" для пропуска'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = ' Задания'
        ordering = ('pk',)


class Answer(models.Model):
    """Модель варианта ответа."""

    text = models.CharField('Текст ответа', max_length=400)
    right = models.BooleanField('Верный ответ', default=False)
    exercise = models.ForeignKey(
        verbose_name='Вариант ответа',
        to='Exercise',
        on_delete=models.CASCADE,
        related_name='answers'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('pk',)
