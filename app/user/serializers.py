"""Serializers for the user API view
"""

from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext as _

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


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token

    Args:
        serializers (_type_): _description_
    """
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'Password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user

        Args:
            attrs (_type_): _description_
        """
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code="authorization")

        attrs['user'] = user
        return attrs
