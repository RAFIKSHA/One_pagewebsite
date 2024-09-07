from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"index.html")
def aboutus(request):
    return HttpResponse("Welcome to the St john")