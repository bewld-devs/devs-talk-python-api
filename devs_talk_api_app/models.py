import uuid
from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.contrib.auth.models import PermissionsMixin


GENDER = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Nonbinary','NONBINARY'),
    ('N/A','N/A'),
)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user
    
    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return  self.email

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True




class CustomUser(AbstractBaseUser, PermissionsMixin):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,)
    username = models.CharField(max_length=19, null = True, blank = True, unique=True)    
    phone_number = models.CharField(max_length=19, null = True, blank = True)
    avatar = CloudinaryField('image', folder='devs-talk-python-api')
    gender = models.CharField(choices=GENDER, max_length=55, null=True, blank=True)
    bio = models.TextField(max_length=120, null=True)
    is_user = models.BooleanField(default=False)
    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    location = models.CharField(max_length=55, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    ordering = ('email',)
    list_display = ('username', 'first_name', 'last_name', 'email', 'gender')
    
     
    
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    objects = UserAccountManager()
    
    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return  self.email

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def natural_key(self):
        return self.email

  

class Staff(models.Model):
    staff = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=150)

    def __str__(self):
        return self.staff.first_name
    

# class User(models.Model):
#     buyer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.buyer.first_name
