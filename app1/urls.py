from django.contrib import admin
from django.urls import path, include
from app1 import views
from .views import SchoolData, StudentDAta, school

urlpatterns = [
    path("api/SchoolData/", views.SchoolData.as_view()),
    path("api/StudentDAta/", views.StudentDAta.as_view()),
    path("api/school/", views.school),
]
