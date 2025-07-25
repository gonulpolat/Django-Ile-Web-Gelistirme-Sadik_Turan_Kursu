from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from Courses.forms import CourseCreateForm
from .models import Category, Course

def index(request):
    courses = Course.objects.all().order_by('date')
    categories = Category.objects.all()   

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'all_courses': courses,
    })


def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        q = request.GET['q']
        courses = Course.objects.filter(isActive=True, title__contains=q).order_by('date')
        categories = Category.objects.all()
    else:
        return redirect('/kurs')

    return render(request, 'courses/search.html', {
        'categories': categories,
        'courses': courses,
    })

def create_course(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect("/kurs")
        
    else:
        form = CourseCreateForm()

    return render(request, "courses/create-course.html", {
        'form': form
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


    return render(request, 'courses/list.html', {
        'categories': categories,
        'courses': courses,
        'page_obj': page_obj,
        'selected_category': slug,
        'all_courses': all_courses,
    })

