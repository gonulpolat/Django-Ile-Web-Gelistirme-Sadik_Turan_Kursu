from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    descriptipon = models.TextField(null=True)
    imageUrl = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True, blank=True)
    isActive = models.BooleanField()
    isUpdated = models.BooleanField()