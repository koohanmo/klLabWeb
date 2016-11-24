from django.db import models
from django.utils import timezone

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField()


class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    msg = models.TextField(blank=False)

