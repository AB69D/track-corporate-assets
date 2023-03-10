from django.db import models
from company.models import *
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

# this is employee table 
class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
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
    # image = models.ImageField(upload_to='Employee')
    return_time = models.CharField(max_length=100)
    is_return = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
# type of payment are include here
PAYMENT_METHOD = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('PayPal', 'PayPal'),
    ('SSLcommerz', 'SSLcommerz'),
)


# payment class connected with user table 
class payment_way(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length= 30, choices=PAYMENT_METHOD, default='Cash on Delivery')

    def __str__(self):
        return self.user.username
    


class Device_Return(BaseModel):
    employee_name = models.CharField(max_length=100, null=True, blank=True)
    device_name = models.ForeignKey(Device, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return self.employee_name