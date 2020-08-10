from django.shortcuts import render
from django.http import HttpResponse

def trail(request):
    return HttpResponse("<h1>project done</h1>")
# Create your views here.
def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def download(request):
    return render(request,"download.html")

def document(request):
    return render(request,"document.html")

def get_demo(request):
    return render(request,"get_demo.html")
