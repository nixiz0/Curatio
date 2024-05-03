from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def credits(request):
    return render(request, "credits.html")

def documentation(request):
    return render(request, "documentation.html")