from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    imageUrl = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True, blank=True)
    isActive = models.BooleanField()
    isUpdated = models.BooleanField()
    slug = models.SlugField(blank=True, db_index=True, default='', editable=False, null=False, unique=True)
    # category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)     # Bir kategori silindiğinde onla ilgili alan null değer alır
    # category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)  # Bir kategori silindiğinde onla ilgili alan 1 değerini alır
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)        # Bir kategori silindiğinde onla ilişikili olan tüm Kurslar da silinir. default parametresi veri tabanında kayıt olduğu için kullanıldı

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.title}"
    