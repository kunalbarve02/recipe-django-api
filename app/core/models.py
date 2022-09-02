"""
DB models
"""
from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,
        BaseUserManager,
        PermissionsMixin
    )


class UserManager(BaseUserManager):
    """Manager for user

    Args:
        BaseUserManager (_type_): _description_
"""

    def create_user(self, email, password, **extra_fields):
        """Function to create save return new user

        Args:
            email (EmailField): Email of user
            password (CharField): Password of
            the user
            **extra_fields : Other fields od
            user models which need not to be mentioned in the args
        """
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system

    Args:
        AbstractBaseUser (In built Class for Auth): Functionality
        for auth system
        PermissionsMixin (In built Class for Auth): permissions
        and field
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
