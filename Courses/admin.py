from django.contrib import admin
from .models import Category, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'isActive', 'isUpdated')    
    list_display_links = ('title', 'slug')                      
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('isActive', 'isUpdated', 'category')
    list_editable = ('isActive',)                                
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',),}


