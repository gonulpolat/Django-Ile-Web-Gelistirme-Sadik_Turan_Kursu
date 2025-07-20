from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists),
    path('liste', views.lists),
    path('detay', views.details),
    path('<category>', views.get_courses_by_category),
]
