from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import render


class APICourseViewSet(ReadOnlyModelViewSet):
    """Cписок курсов, и отдельный курс по pk."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


def login_view(request):
    return render(request, 'login/login.html')
