from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PlatformUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,
    null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name