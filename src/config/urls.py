from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/v1/', include([
        path('', include('courses.urls')),
        path('', include('users.urls')),
    ])),
    path('admin/', admin.site.urls),
    # * Авторизация
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    # * Документация
    path('', include('spectacular.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
