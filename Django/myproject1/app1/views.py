from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogd(request):
    return HttpResponse("My blog page!!") 