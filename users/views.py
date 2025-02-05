from django.shortcuts import render
from django.http import request

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')
# Create your views here.