import re
from turtle import ht
from django.shortcuts import render, HttpResponse
from templates.models import Drug

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is the homepage')
def signin(request):
    return render(request, 'signin.html')
def explore(request):
    return render(request, 'explore.html')
def drug(request):
    drugs = Drug.objects.all()
    return render(request, 'drug_list.html', {'drugs': drugs})