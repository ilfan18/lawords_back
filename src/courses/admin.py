from django.contrib import admin
from django.utils.html import format_html
from . import models


class LessonInline(admin.StackedInline):
    model = models.Lesson
    extra = 0


class ExerciseInline(admin.StackedInline):
    model = models.Exercise
    extra = 0


class AnswerInline(admin.StackedInline):
    model = models.Answer
    extra = 0


@admin.register(models.Course)
class CoursesAdmin(admin.ModelAdmin):

    def icon_tag(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width:48px; height:48px;" />'.format(obj.icon.url))
        return

    icon_tag.short_description = 'Иконка курса'

    list_display = ('name', 'level', 'icon_tag')
    search_fields = ('name', 'level')
    list_filter = ('level',)
    inlines = [LessonInline]


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):

    def icon_tag(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width:48px; height:48px;" />'.format(obj.icon.url))
        return

    icon_tag.short_description = 'Иконка урока'

    list_display = ('name', 'icon_tag')
    search_fields = ('name',)
    list_filter = ('course',)
    inlines = [ExerciseInline]


@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('lesson',)
    inlines = [AnswerInline]
