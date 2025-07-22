from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    imageUrl = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True, blank=True)
    isActive = models.BooleanField()
    isUpdated = models.BooleanField()


    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60)