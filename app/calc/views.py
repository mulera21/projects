from django.shortcuts import render



def home(request):
    return render(request, "calc/home.html",{"name":"edmond"})
def nice(request):
    return render(request, "calc/about.html", {"school":"angayu"})