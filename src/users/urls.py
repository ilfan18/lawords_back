from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserViewSet,
    UserMeView
)

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('me/', UserMeView.as_view(), name='user-me'),
]
urlpatterns += router.urls
