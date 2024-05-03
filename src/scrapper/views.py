from django.shortcuts import render


# Create your views here.
def scrapper(request):
    return render(request, "scrapper.html")