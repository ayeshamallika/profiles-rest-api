from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user proflie"""
    def create_user(self,email,name,password=None):
        """create new user profile """
        if not email:
            raise ValueError('User must have email adress')

        email = self.normalize_email(email)
        user = self.model(email=email ,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email,name,password):
        """Create and save new super user"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.save(using=self._db)

        return user

class UserProflie(AbstractBaseUser,PermissionsMixin):
    """DataBase model for users in system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active =models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrive full name of user"""
        return self.name
    def short_name(self):
        """ Retrive short name """
        return short_name
    def _str_(self):
        """Retrive string representation of user """
