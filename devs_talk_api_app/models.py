# from enum import unique
# from tokenize import blank_re
# import uuid
from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save


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
    username = models.CharField(max_length=19, null = True, blank = True, unique=True)    
    gender = models.CharField(choices=GENDER, max_length=55, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=40, null = True, blank = True)
    last_name = models.CharField(_('last name'), max_length=50, null = True, blank = True)
    email = models.EmailField(_('email address'), unique=True)
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

class Education(models.Model):
    school = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    fieldOfStudy = models.CharField(max_length=50)
    dateFrom = models.DateField(auto_now=False, auto_now_add=False)
    dateTo = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    current = models.BooleanField(default=False)
    graduated = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.fieldOfStudy
        
class Work(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    responsibilities = models.TextField(max_length=255)
    location = models.CharField(max_length=50)
    dateFrom = models.DateField(auto_now=False, auto_now_add=False)
    dateTo = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    current = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Work'

    def __str__(self):
        return self.role


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(max_length=8, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    education = models.ForeignKey(Education, blank=True, null=True, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, blank=True, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=55, null=True, blank=True)
    avatar = CloudinaryField('image', null=True, folder='devs-talk-python-api-avatars')
    cover_photo = CloudinaryField('image', null=True, folder='devs-talk-python-api-cover-photos')

    def __str__(self):
        return f'{self.user.username} Profile'
  

class Staff(models.Model):
    staff = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=150)

    def __str__(self):
        return self.staff.first_name
    


@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()