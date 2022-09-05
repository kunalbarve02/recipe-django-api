"""Views for the user API
"""
from rest_framework import generics

from user.serializers import UserSerializers


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system

    Args:
        generics: Handles a post request which is designed for creating objects
    """
    serializer_class = UserSerializers
