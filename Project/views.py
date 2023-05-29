from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def allprojects(request):
    return render(request, "Projects/projects.html")
