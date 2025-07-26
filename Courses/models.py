from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', null=False, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    imageUrl = models.CharField(max_length=50, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    isUpdated = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, db_index=True, default='', null=False, unique=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"
    
class UploadModel(models.Model):
    image = models.ImageField(upload_to='images')
    