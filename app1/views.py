from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .serializers import SchoolSerializers, StudentSerializers
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

# from rest_framework.relations import ForeignKey
import json
from app1.models import School, Student

# def home(request):
#     return HttpResponse("hello")

# Create your views here.


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.prefetch_related('comments_rel').all()

    serializer_class = SchoolSerializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("School_name1").all()

    serializer_class = StudentSerializers


class SchoolData(APIView):
    def get(request, self):
        pi = School.objects.all().values()
        return JsonResponse(list(pi), safe=False)


# class Model_A_View(viewsets.ModelViewSet):
#     serializer_class =StudentSerializers
#     queryset = SchoolSerializers.objects.select_related('model_b').all()


class StudentDAta(APIView):
    def get(request, self):
        pi = Student.objects.all().values()
        return JsonResponse(list(pi), safe=False)


def school(request):
    # books=Student.objects.all().values()

    data = []     
    # book = Student.objects.all().prefetch_related('School_name1')
    # for post in book:
    #     School_name = post.School_name1.class_strength
    #     data.append(School_name)

    book=Student.objects.all().select_related()
    data=[post.School_name1.school_name for post in book]
    #data = json.loads(book)
    #books=[post.comments_rel for post in book]
    return JsonResponse((data), safe=False)

    return HttpResponse(request, "app1/home.html", {"dada": dada})
