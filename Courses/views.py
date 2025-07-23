from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Category, Course

data = {
    'programlama': 'Programlama Kategorisine Ait Kurslar',
    'web-gelistirme': 'Web Geliştirme Kategorisine Ait Kurslar',
    'mobil-uygulama': 'Mobil Uygulama Kategorisine Ait Kurslar',
}

def index(request):
    courses = Course.objects.all()
    categories = Category.objects.all()    

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'all_courses': courses,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def get_courses_by_category(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True)
    all_courses = Course.objects.all()
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'selected_category': slug,
        'all_courses': all_courses,
    })

