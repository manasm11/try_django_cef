from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email: raise ValueError('User must have an email')
        email = self.normalize_email(email)
        if not name: raise ValueError('User must have an name')
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        if not password: raise ValueError('Superuser must have password')
        if not name: raise ValueError('Superuser must have name')
        if not email: raise ValueError('Superuser must have email')
        user = self.create_user(email, name)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email