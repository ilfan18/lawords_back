from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Course
from .serializers import CourseSerializer


class APICourseViewSet(ReadOnlyModelViewSet):
    """Контроллер выдает список курсов, и отдельный курс по pk."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
