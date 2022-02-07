

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# each view takes at least one HttpResponse object and returns one
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>Rango says here is the about page.")