from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
    )

    age = models.PositiveIntegerField(
        verbose_name='возраст',
    )

    email = models.EmailField(
        verbose_name='почта',
        unique=True,
    )
