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
    slug = models.SlugField(blank=True, db_index=True, default='', editable=False, null=False, unique=True)
    """
    blank    -> form ile ilgili
                True: boş olabilir / False: boş olamaz
    null     -> veri tabanı ile ilgili
                True: boş olabilir / False: boş olamaz
    default  -> veri tabanı ile ilgili
    editable -> form ile ilgili
                True: alan görünür ve değer girilebilir / False: form üzerinde görünmüyor
    """ 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        # http://127.0.0.1:8000/admin/Courses/course/    => isimler bu fonksiyondan geliyor
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"