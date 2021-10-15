from django.db import models


class Course(models.Model):
    """Модель курса."""

    name = models.CharField('Название курса', max_length=255)
    level_choices = [
        ('beginner', 'Beginner'),
        ('elementary', 'Elementary'),
        ('intermediate', 'Intermediate'),
        ('upper_intermediate', 'Upper-Intermediate'),
        ('advanced', 'Advanced'),
    ]
    level = models.CharField('Уровень курса', blank=True,
                             max_length=255, choices=level_choices, default='beginner')
    new_words = models.IntegerField(
        'Число новых слов', null=True, blank=True, default=0)
    icon = models.ImageField(
        'Иконка курса', null=True, blank=True, upload_to='courses/icons/')
    cover = models.ImageField(
        'Обложка курса', null=True, blank=True, upload_to='courses/covers/')

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
        'Иконка урока', null=True, blank=True, upload_to='lessons/icons/')
    cover = models.ImageField(
        'Обложка урока', null=True, blank=True, upload_to='lessons/covers/')
    course = models.ForeignKey(
        to='Course', on_delete=models.CASCADE, related_name='lessons', verbose_name='Урок из курса')

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
        ('word_miss_type', 'Задание с пропуском'),
        ('translate_type', 'Задание с переводом'),
    ]
    exercise_type = models.CharField('Тип задания', blank=True,
                                     max_length=255, choices=type_choices, default='word_miss_type')
    lesson = models.ForeignKey(
        to='Lesson', on_delete=models.CASCADE, related_name='exercises', verbose_name='Задание из урока')
    text = models.TextField('Текст вопроса', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = ' Задания'
        ordering = ('pk',)


class Answer(models.Model):
    text = models.CharField(
        'Текст ответа', max_length=400)
    right = models.BooleanField('Верный ответ', default=False)
    exercise = models.ForeignKey(
        to='Exercise', on_delete=models.CASCADE, related_name='answers', verbose_name='Вариант ответа')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('pk',)
