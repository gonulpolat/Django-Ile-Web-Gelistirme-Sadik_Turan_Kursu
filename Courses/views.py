from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def lists(request):
    return HttpResponse('Kurs Listesi')

def details(request):
    return HttpResponse('Kurs Detay Sayfası')

def programming(request):
    return HttpResponse('Programlama Sayfası')

def mobile_apps(request):
    return HttpResponse('Mobil Uygulama Sayfası')