from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Allows Django to work with our custom user model"""

    def create_user(self, email, name, password = None):
        """Create a new user profile object"""

        if not email:
            raise ValueError('Users must have an email address')

        #Normalizes email address to a standard form
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        #Saves password as a hash
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves new superuser given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile within our system."""

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    #Required subsitutions
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    #Default set to Required
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #Required
    def get_full_name(self):
        """Used to retrieve a users full name."""
        return self.name

    def get_short_name(self):
        """Used to get a users short name."""
        return self.name

    def __str__(self):
        """Django uses this to convert object to a string"""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return model as string"""

        return self.status_text
