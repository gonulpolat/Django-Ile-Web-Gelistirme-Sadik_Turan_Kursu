from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    imageUrl = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True, blank=True)
    isActive = models.BooleanField()
    isUpdated = models.BooleanField()
    slug = models.SlugField(db_index=True, default='', null=False, unique=True)    # yani önceki verilere boş karakter gir

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60)