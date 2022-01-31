from django.shortcuts import render
from django.http import HttpResponse

def calculate():
  x = 1
  y = 2
  return x

# Create your views here.
def index(request):
  return HttpResponse("Hello, world!")

def brian(request):
  return HttpResponse("Hello, Brian!")

def greet(request, name):
  return HttpResponse(f"Hello, {name.capitalize()}!")

def say_hello(request):
  x = calculate()
  return render(request, 'hello.html', {'name': 'Django'})
