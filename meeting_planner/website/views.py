from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HOME:")
def welcome(request):
    return HttpResponse("<h1>----WELCOME---- TO____THIS----- PAGE:</h1> <a href='/'>BACK</a>")

