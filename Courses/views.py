from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test

from Courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Category, Course, UploadModel, Slider

def index(request):
    courses = Course.objects.all().order_by('date')
    categories = Category.objects.all() 
    sliders = Slider.objects.filter(is_active = True)  

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'all_courses': courses,
        'sliders': sliders,
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

"""
    Gelen URL: http://127.0.0.1:8000/accounts/login/?next=/kurs/course-create
    Fakat bu uygulamada account kullanıyoruz. settings içinden değiş.
"""

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def course_create(request):
    # if not request.user.is_superuser:
    #     return redirect('index')
    if request.method == 'POST':
        form = CourseCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

            return redirect("/kurs")
        
    else:
        form = CourseCreateForm()

    return render(request, "courses/course-create.html", {
        'form': form
    })

@login_required()
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses': courses
    })

@user_passes_test(isAdmin)
def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == 'POST':
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render(request, "courses/course-edit.html", {
        'form': form,
    })

@user_passes_test(isAdmin)
def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == 'POST':
        # Course.objects.get(pk=id).delete()    # kursu yukarda alıyorsun zaten, bir daha almaya gerek yok
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course-delete.html", {
        'course': course,
    })


def upload(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES['image'])
            model.save()
            return render(request, "courses/success.html")
    
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {
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

