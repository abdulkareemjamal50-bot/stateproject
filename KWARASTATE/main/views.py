from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render (request, "about.html")

def contact(request):
    return render (request, "contact.html")

def government(request):
    return render (request, "government.html")

def project(request):
    return render (request, "project.html")

def ministries(request):
    return render (request, "ministries.html")

def services(request):
    return render (request, "services.html")

def investment(request):
    return render (request, "investment.html")

def tourism(request):
    return render (request, "tourism.html")


def news(request):
    return render (request, "news.html")