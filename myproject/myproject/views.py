#from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    #return HttpResponse("hello world, I am back")
    return render(request, 'home.html')

def About(request):
    #return HttpResponse("this the learning page")
    return render(request, 'about.html')