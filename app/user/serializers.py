"""Serializers for the user API view
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    """Serializers for the user object

    Args:
        serializers : takes json -> validates ->
        python object/model in datatabase

    Returns:
        _type_: _description_
    """
    class Meta:
        """Model and fields passed through serializer
        """
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password':
            {
                'write_only': True,
                'min_length': 5
            }
        }  # keyword aargs

    def create(self, validated_data):
        """Create and return a user with encrypted password.

        Args:
            validated_data (_type_): _description_
        """
        return get_user_model().objects.create_user(**validated_data)
