from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pizzeria(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.owner.first_name



class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField(default=None)
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.
                                CASCADE, default='1')

    def __str__(self):
        return self.title

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.
                                 CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.first_name