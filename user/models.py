from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, unique=True, max_length=120)
    password = models.CharField(null=True, blank=True, max_length=120)
    name = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True,null=True)
    point = models.IntegerField(blank=True, null=False, default=0)

    is_superuser = models.BooleanField(blank=True, null=False, default=False) #使用admin
    is_staff = models.BooleanField(blank=True, null=False, default=False) #進入admin
    is_active = models.BooleanField(blank=True, null=False, default=True) #可使用的帳號

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return self.email