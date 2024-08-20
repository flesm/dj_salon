from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from salon.models import CourseModel


def index(request):
    courses = CourseModel.objects.all()
    return render(request, 'salon/index.html', {'courses': courses[:3]})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Старонка не знойдзена</h1>")


def mini_courses(request):
    return render(request, 'salon/includes/mini_course.html')


def all_courses(request):
    courses = CourseModel.objects.all()
    return render(request, 'salon/all_courses.html', {'courses': courses})
