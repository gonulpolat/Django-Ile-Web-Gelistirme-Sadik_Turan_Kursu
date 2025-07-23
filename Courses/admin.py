from django.contrib import admin
from .models import Category, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'isActive', 'isUpdated')    # http://127.0.0.1:8000/admin/Courses/course/ sayfasında görünecek alanlar
    list_display_links = ('title', 'slug')                       # başta sadece title linkti
    readonly_fields = ('slug',)                                  # model içinde slug alanı için editable=False dediğin zaman slug alanı görünmüyordu, şimdi görünür ancak değiştirilemez
    list_filter = ('isActive', 'isUpdated')
    list_editable = ('isActive',)                                # kurs detayına gitmeden değitirmek için
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Course, CourseAdmin)