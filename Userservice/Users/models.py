from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    firstName=models.CharField(max_length=256)
    lastName=models.CharField(max_length=256)
    email=models.EmailField()
    password=models.CharField(max_length=256)
    phoneNo=models.CharField(max_length=14)

    def __str__(self):
        return f"{self.first_name} {self.lastName}"
