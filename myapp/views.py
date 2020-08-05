from django.shortcuts import render
from django.http import HttpResponse

def trail(request):
    return HttpResponse("<h1>project done</h1>")
# Create your views here.
def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home.html")

def profile(request):
    name="Aditya"
    return render(request,"profile.html",{"name":name})
