from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gowthami(request):
    return HttpResponse('<h1> this view belongs to gowthami</h1>')


