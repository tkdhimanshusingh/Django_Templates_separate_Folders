from django.contrib import admin
from django.urls import path

from course.views import course_django, course_python

urlpatterns = [
    path('learndj/',course_django),
    path('learnpy/',course_python),
]
