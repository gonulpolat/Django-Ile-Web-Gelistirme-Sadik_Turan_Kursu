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
        'courses': courses
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def get_courses_by_category_name(request, category_name):
    try: 
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text,
        })
    except:
        return HttpResponseNotFound('<h1>Yanlış Kategori Seçimi</h1>')

def get_courses_by_category_id(request, category_id):
    category_key_list = list(data.keys())
    if category_id > len(category_key_list):
        return HttpResponseNotFound('<h1>Yanlış Kategori Seçimi</h1>')
    category_name = category_key_list[category_id - 1]

    redirect_url = reverse('courses_by_category_name', args=[category_name])

    return redirect(redirect_url)