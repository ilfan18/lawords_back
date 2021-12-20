from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserViewSet,
    UserMeView,
    UserMeSetUsernameView,
    UserMeSetPasswordView
)

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('me/', UserMeView.as_view(), name='user-me'),
    path('me/set_username/', UserMeSetUsernameView.as_view(),
         name='user-me-username-set'),
    path('me/set_password/', UserMeSetPasswordView.as_view(),
         name='user-me-password-set'),
]
urlpatterns += router.urls
