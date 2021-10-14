from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Lesson, Exercise, Answer


class LessonAdmin(admin.StackedInline):
    model = Lesson
    extra = 0


class ExerciseInline(admin.StackedInline):
    model = Exercise
    extra = 0


class Answerinline(admin.StackedInline):
    model = Answer
    extra = 0


class CoursesAdmin(admin.ModelAdmin):

    model = Course

    def icon_tag(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width:48px; height:48px;" />'.format(obj.icon.url))
        return

    icon_tag.short_description = 'Иконка курса'

    list_display = ('name', 'level', 'icon_tag')
    search_fields = ('name', 'level')
    list_filter = ('level',)
    inlines = [
        LessonAdmin,
    ]


class LessonAdmin(admin.ModelAdmin):
    model = Lesson

    def icon_tag(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width:48px; height:48px;" />'.format(obj.icon.url))
        return

    icon_tag.short_description = 'Иконка урока'

    list_display = ('name', 'icon_tag')
    search_fields = ('name',)
    list_filter = ('course',)
    inlines = [ExerciseInline]


class ExerciseAdmin(admin.ModelAdmin):
    model = Exercise

    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('lesson',)
    inlines = [
        Answerinline,
    ]


admin.site.register(Course, CoursesAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exercise, ExerciseAdmin)
