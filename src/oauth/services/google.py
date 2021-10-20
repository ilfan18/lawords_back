from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
from ..models import AuthUser
from .. import serializers
from . import base_auth


def check_google_auth(google_user: serializers.GoogleAuth) -> dict:
    try:
        id_token.verify_oauth2_token(
            google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad Google token')

    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])

    return base_auth.create_token(user.id)
