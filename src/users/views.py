from rest_framework import views, viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    SetUsernameSerializer,
    SetPasswordSerializer,
)
from .services import send_activation_email


class UserViewSet(viewsets.ModelViewSet):
    """User view set"""

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        send_activation_email(user, request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


def activate(request, uidb64, token):
    return HttpResponse('Thank you for your email confirmation. Now you can login your account.')


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
    """Edit current user's username."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SetUsernameSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
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


class UserMeSetPasswordView(views.APIView):
    """Edit current user's password."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        user = request.user
        if serializer.is_valid():
            new_password = serializer.data['new_password']
            user.set_password(new_password)
            user.save()
            response = UserSerializer(user)
            return Response(response.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
