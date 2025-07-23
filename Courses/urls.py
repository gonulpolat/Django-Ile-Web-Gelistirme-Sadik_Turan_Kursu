from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>', views.details, name='course_details'),
    path('kategori/<slug:slug>', views.get_courses_by_category, name='courses_by_category_name'),
]
