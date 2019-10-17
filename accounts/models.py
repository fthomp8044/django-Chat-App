from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank= True)
    location= models.CharField(max_length=30, blank=True)
    #/images
    avatar = models.ImageField(upload_to=None)

    def __str__(self):
        return self.user.username
