from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists),
    path('liste', views.lists),
    path('detay', views.details),
    path('programlama', views.programming),
    path('mobil-uygulamalar', views.mobile_apps),
]
