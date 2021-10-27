from django.db import models


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
    course = models.ForeignKey(
        verbose_name='Урок из курса',
        to='Course',
        on_delete=models.CASCADE,
        related_name='lessons',
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
    type_choices = [
        ('', 'Выберите тип задания'),
        ('word_miss_type', 'Задание с пропуском'),
        ('translate_type', 'Задание с переводом'),
    ]
    exercise_type = models.CharField(
        'Тип задания',
        max_length=255,
        choices=type_choices,
        default='word_miss_type',
        blank=True
    )
    lesson = models.ForeignKey(
        verbose_name='Задание из урока',
        to='Lesson',
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    text = models.TextField('Текст вопроса', max_length=500)

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
