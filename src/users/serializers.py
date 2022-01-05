from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from .models import UserLesson
from courses.models import Lesson, Course
# ! Про это узнать
from django.db import transaction


class UserLessonSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='lesson.id')

    class Meta:
        model = UserLesson
        fields = ('score', 'id')


class UserSerializer(serializers.ModelSerializer):
    lessons = UserLessonSerializer(source='userlesson_set', many=True)

    @transaction.atomic
    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        if 'lessons' in self.initial_data:
            lessons = self.initial_data.get('lessons')
            for lesson in lessons:
                id = lesson.get('id')
                score = lesson.get('score')
                new_lesson = Lesson.objects.get(pk=id)
                UserLesson(user=instance, lesson=new_lesson,
                           score=score).save()
        user.save()
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        #! Разнести по разным сериализаторам
        #! Может добавить несколько одинаковых
        if 'lessons' in self.initial_data:
            UserLesson.objects.filter(user=instance).delete()
            lessons = self.initial_data.get('lessons')

            for lesson in lessons:
                id = lesson.get('id')
                score = lesson.get('score')
                new_lesson = Lesson.objects.get(pk=id)
                UserLesson(user=instance, lesson=new_lesson,
                           score=score).save()
                #! Это что вообще за треш я написал
                course = new_lesson.course
                if (course not in instance.courses.all()):
                    print('1')
                    course_lessons = new_lesson.course.lessons.all()
                    user_lessons = instance.lessons.all()
                    intersection_lessons = set(
                        user_lessons).intersection(set(course_lessons))
                    if set(course_lessons) == intersection_lessons:
                        instance.courses.add(course)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    class Meta:
        model = get_user_model()
        exclude = (
            'password',
            'is_superuser',
            'is_staff',
            'date_joined',
            'last_login',
            'groups',
            'user_permissions',
        )


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_username'] = self.fields.pop('username')

    def save(self, **kwargs):
        kwargs['username'] = self.validated_data.get('new_username')
        return super().save(**kwargs)


class PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):

        user = self.context["request"].user or self.user
        # why assert? There are ValidationError / fail everywhere
        assert user is not None
        try:
            validate_password(attrs['new_password'], user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)})
        return super().validate(attrs)


class CurrentPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={'input_type': 'password'})

    default_error_messages = {
        'invalid_password': _('Current password is not vallid.')
    }

    def validate(self, attrs):
        is_password_valid = self.context['request'].user.check_password(
            attrs['current_password'])
        if is_password_valid:
            return super().validate(attrs)
        else:
            raise serializers.ValidationError(
                {"current_password": _('Current password isn`t correct.')})


class SetPasswordSerializer(PasswordSerializer, CurrentPasswordSerializer):
    pass


class SetUsernameSerializer(UsernameSerializer, CurrentPasswordSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'current_password')
