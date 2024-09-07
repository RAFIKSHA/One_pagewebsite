from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    data={
         'name':"rafik",
         'phone':7028352298,
         'clist':[1,5,4,6,8,9,6,3]
         }

    return render(request,"index.html",data)

# def aboutus(request):
#     return HttpResponse("Welcome to the St john")