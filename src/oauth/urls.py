from django.urls import path, include
from .endpoints import views, auth_views


urlpatterns = [
    # * Это временно
    path('', auth_views.google_login),
    path('google/', auth_views.google_auth),
]
