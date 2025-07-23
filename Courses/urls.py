from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name='course_details'),
    path('kategori/<int:category_id>', views.get_courses_by_category_id, name='courses_by_category_id'),
    path('kategori/<str:category_name>', views.get_courses_by_category_name, name='courses_by_category_name'),
]
