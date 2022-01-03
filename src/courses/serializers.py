from rest_framework import serializers
from .models import Course, Lesson, Exercise, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'right', 'id']


class ExerciseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ['title', 'exercise_type', 'text', 'answers', 'id', 'image']


class LessonSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'icon', 'cover',
                  'exercises', 'main_text', 'top_text']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'level',
            'new_words',
            'icon',
            'cover',
            'lessons'
        )
