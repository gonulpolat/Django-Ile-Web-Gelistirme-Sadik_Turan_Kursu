from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('anasayfa', views.home),
    path('iletisim', views.contact),
    path('hakkimizda', views.about),
]