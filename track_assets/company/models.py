from django.db import models

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='Device')

    def __str__(self) -> str:
        return self.name
    