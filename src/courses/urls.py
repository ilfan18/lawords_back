from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/courses/', api_all_courses)
]
