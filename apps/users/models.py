from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female")
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="nickname", default="")
    birthday = models.DateField(verbose_name="birthday", blank=True, null=True)
    gender = models.CharField(max_length=6, verbose_name="gender", choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, verbose_name="address", default="")
    mobile = models.CharField(max_length=11, unique=True, verbose_name="mobile number")
    avatar = models.ImageField(upload_to="avatar/%Y/%m", verbose_name="avatar", default="default.jpg")

    class Meta:
        verbose_name = "user information"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        return self.username


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        abstract = True
