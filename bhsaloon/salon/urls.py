from django.urls import path
from salon import views

urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.all_courses, name='courses'),
]