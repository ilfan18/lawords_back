from rest_framework import views, viewsets, generics, status
from rest_framework.response import Response
from rest_framework import permissions
from .models import User
from .serializers import (
    UserSerializer,
    SetUsernameSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """User view set"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeView(views.APIView):
    """View to represent current user."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        """Get current user."""
        serializer = self.serializer_class(
            self.get_object(),
            context={'request': request}
        )
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request):
        """Update current user."""

        serializer = self.serializer_class(
            self.get_object(),
            data=request.data,
            context={'request': request}
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, request):
        """Partial update current user."""

        serializer = self.serializer_class(
            self.get_object(),
            data=request.data,
            partial=True,
            context={'request': request}
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request):
        """Destroy current user."""
        request.user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def get_object(self):
        return self.request.user


class UserMeSetUsernameView(views.APIView):
    """Edit current user's password."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SetUsernameSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        if serializer.is_valid():
            new_username = serializer.data['new_username']
            setattr(user, 'username', new_username)
            user.save()
            response = UserSerializer(user)
            return Response(response.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
