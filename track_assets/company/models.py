from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

# device table user as a foreignkey
class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True) 
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='device')

    def __str__(self) -> str:
        return self.name
    