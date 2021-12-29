from rest_framework import views, viewsets, status
from rest_framework import permissions
from .models import Course, Lesson
from .serializers import (
    CourseSerializer,
    LessonSerializer
)
from django.shortcuts import render


class APICourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Courses list and particular course by id."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class APILessonViewSet(viewsets.ReadOnlyModelViewSet):
    """List of lissons by provided course id."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
