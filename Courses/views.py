from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from .models import Category, Course

def index(request):
    courses = Course.objects.all()
    categories = Category.objects.all()   

    paginator = Paginator(courses, len(courses))
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page) 

    print(paginator.count)
    print(paginator.num_pages)

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'all_courses': courses,
        'page_obj': page_obj,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def get_courses_by_category(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True).order_by('date')
    all_courses = Course.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(courses, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)


    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'page_obj': page_obj,
        'selected_category': slug,
        'all_courses': all_courses,
    })

