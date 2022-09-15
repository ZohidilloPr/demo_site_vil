from django.db import models
from .menegars import CustomUsersMenegar
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class Users(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, verbose_name="F.I.SH", null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True, verbose_name="Telefon raqam")
    username = models.CharField(max_length=100, unique=True, verbose_name="Username*")
    joined_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True, verbose_name="Active")
    superuser = models.BooleanField(default=False, verbose_name="SuperAdmin")
    staff = models.BooleanField(default=False, verbose_name="xodim")
    data_add = models.BooleanField(default=False, verbose_name="Malumot to'ldiruvchi")
    data_viewer = models.BooleanField(default=False, verbose_name="Malumotlarni kuzatuvchi")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return self.full_name
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_info(self):
        return f"F.I.SH: {self.get_full_name}, \nTelefon raqam: {self.get_phone_number} \nUsername: {self.username}"

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.superuser
    
    @property
    def is_data_viewer(self):
        return self.data_viewer
    
    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_superuser

    objects = CustomUsersMenegar()