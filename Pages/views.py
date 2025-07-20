from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Anasayfa')

def contact(request):
    return HttpResponse('İletişim Sayfası')

def about(request):
    return HttpResponse('Hakkımızda Sayfası')
