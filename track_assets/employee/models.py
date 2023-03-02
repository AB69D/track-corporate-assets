from django.db import models
from company.models import *
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=14, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    given_time  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Employee')
    return_time = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

