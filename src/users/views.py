from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions


@api_view(['POST'])
def verify_token(request):
    print(request)
