from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.user.username