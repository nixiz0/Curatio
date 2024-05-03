# Create your models here
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField
from django.db import models


class CuratioUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, country, password=None):
        if not email:
            raise ValueError('You must provide an email address')
        if not firstname:
            raise ValueError('You must provide a firstname')
        if not lastname:
            raise ValueError('You must provide a lastname')
        if not country:
            raise ValueError('You must provide a country')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            country=country,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, firstname, lastname, country, password=None):
        user = self.create_user(email=email, password=password, firstname=firstname, lastname=lastname, country=country)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CuratioUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    country = CountryField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname", "country"]
    objects = CuratioUserManager()
    
    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module_perms(self, app_label):
        return True