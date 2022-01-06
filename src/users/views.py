from .services import (
    send_activation_email,
    get_user_uidb64
)
from .serializers import (
    UserSerializer,
    SetUsernameSerializer,
    SetPasswordSerializer,
    UserCreateSerializer
)
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework import views, viewsets, status


class UserViewSet(viewsets.ModelViewSet):
    """User view set"""

    #! Перенести все сюда (как в Djoser)

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        user = serializer.save()
        # ! Переделать в класс от стандартного класса
        send_activation_email(self.request, user)


@api_view(('POST',))
def user_activate(request):
    """Activate user. Takes uidb64 and token"""
    user = get_user_uidb64(request.data.get('uid'))
    if user and default_token_generator.check_token(user, request.data.get('token')):
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
def resend_activation(request):
    """Resend activation email. Takes uid."""
    try:
        user = get_user_model(). _default_manager.get(pk=request.data.get('uid'))
    except(User.DoesNotExist):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user.is_active = False
    user.save()
    send_activation_email(request, user)
    return Response(status=status.HTTP_200_OK)


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
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
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
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
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
            return Response(response.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


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
            return Response(response.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
