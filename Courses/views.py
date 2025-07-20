from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def lists(request):
    return HttpResponse('Kurs Listesi')

def details(request, course_name):
    return HttpResponse(f'{course_name.capitalize()} Detay Sayfası')

def get_courses_by_category_name(request, category_name):
    text = ""
    if category_name == "programlama":
        text = "Programlama Kategorisine Ait Kurslar"
    elif category_name == "web-gelistirme":
        text = "Web Geliştirme Kategorisine Ait Kurslar"
    elif category_name == "mobil-uygulama":
        text = "Mobil Uygulama Kategorisine Ait Kurslar"
    else:
        text = "Yanlış Kategori Seçimi"
    return HttpResponse(text)

def get_courses_by_category_id(request, category_id):
    return HttpResponse(category_id)