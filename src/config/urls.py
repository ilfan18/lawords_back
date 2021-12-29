from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include([
        path('', include('courses.urls')),
    ])),
    path('admin/', admin.site.urls),
    # * Экспирементальная авторизация
    path('auth/', include('users_auth.urls')),
    # * Экспирементальное обслуживание пользователя
    path('users/', include('users.urls')),
    # * Авторизация через соц сети
    path('auth_cosial/', include('rest_framework_social_oauth2.urls')),
    # * Документация
    path('', include('spectacular.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
