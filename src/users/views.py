from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Profile
from .serializers import ProfileInfoSerializer


class APIProfileInfoViewSet(ReadOnlyModelViewSet):
    """Cписок профилей, и отдельный профиль по pk."""
    queryset = Profile.objects.all()
    serializer_class = ProfileInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
