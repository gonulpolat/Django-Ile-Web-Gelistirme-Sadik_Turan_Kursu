from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def lists(request):
    return HttpResponse('Kurs Listesi')

def details(request):
    return HttpResponse('Kurs Detay Sayfası')

def get_courses_by_category(request, category):
    text = ""
    if category == "programlama":
        text = "Programlama Kategorisine Ait Kurslar"
    elif category == "web-gelistirme":
        text = "Web Geliştirme Kategorisine Ait Kurslar"
    elif category == "mobil-uygulama":
        text = "Mobil Uygulama Kategorisine Ait Kurslar"
    else:
        text = "Yanlış Kategori Seçimi"
    
    return HttpResponse(text)