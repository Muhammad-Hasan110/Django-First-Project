from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "name": "Muhammad Hasan",
        "age": "23"
    }
    return render(request,"index.html",context)
    # return HttpResponse("this is Home Page"),
def about(request):
    return HttpResponse("this is About Page"),
def services(request):
    return HttpResponse("this is Services Page"),
def contacts(request):
    return HttpResponse("this is Contacts Page")


