from django.shortcuts import render
from profiles_api.models import Course, UserProfile
import requests
# Create your views here.

def home(request):
    return render(request, 'index.html', {'name': 'test'})


def students(request):
    term = request.GET.get('term', '')
    response = requests.get('http://localhost:8000/api/profile/?term={}'.format(term))
    # students_objs = UserProfile.objects.all()
    students_objs = response.json()
    return render(request, 'students.html', {'students': students_objs, 'term': term})

def courses(request):
    term = request.GET.get('term', '')
    start_date = request.GET.get('start_date', '')
    response = requests.get('http://localhost:8000/api/courses/?term={}&start_date={}'.format(term, start_date))
    courses_objs = response.json()
    #print(courses_objs)
    return render(request, 'courses.html', {'courses': courses_objs, 'name': 'test'})