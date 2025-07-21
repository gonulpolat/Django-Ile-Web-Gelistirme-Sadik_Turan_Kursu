from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    'programlama': 'Programlama Kategorisine Ait Kurslar',
    'web-gelistirme': 'Web Geliştirme Kategorisine Ait Kurslar',
    'mobil-uygulama': 'Mobil Uygulama Kategorisine Ait Kurslar',
}

def index(request):
    category_list = data.keys()

    return render(request, 'courses/index.html', {
        'categories': category_list
    })

def details(request, course_name):
    return HttpResponse(f'{course_name.capitalize()} Detay Sayfası')

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