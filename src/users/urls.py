from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserViewSet,
    UserMeView,
    UserMeSetUsernameView,
    UserMeSetPasswordView,
    user_activate,
    resend_activation
)

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('me/', UserMeView.as_view(), name='user-me'),
    path('me/set_username/', UserMeSetUsernameView.as_view(),
         name='user-me-username-set'),
    path('me/set_password/', UserMeSetPasswordView.as_view(),
         name='user-me-password-set'),
    path('activate/', user_activate, name='activate'),
    path('resend/', resend_activation),
]
urlpatterns += router.urls
