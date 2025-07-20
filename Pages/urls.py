from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('anasayfa', views.index),
    path('index', views.index),
    path('iletisim', views.contact),
    path('hakkimizda', views.about),
]