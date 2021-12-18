from rest_framework import views, viewsets, generics, status
from rest_framework.response import Response
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User view set"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeView(views.APIView):
    """View to represent current user."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get current user."""
        serializer = UserSerializer(self.get_object())
        return Response(serializer.data)

    def put(self, request):
        """Update current user."""

        serializer = UserSerializer(self.get_object(), data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request):
        """Partial update current user."""

        serializer = UserSerializer(
            self.get_object(), data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

    def get_object(self):
        return self.request.user
