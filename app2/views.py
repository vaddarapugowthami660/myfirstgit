from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.

def thriveni(request):
    return HttpResponse('<h2><marquee> she is my best frnd forever</marquee></h2>')

def harshitha(request):
    return HttpResponse('<h3><marquee> she and me good tom and jerry fighting</marquee></h3>')

