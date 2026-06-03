from django.shortcuts import render

# Create your views here.
def state(request):
    return render(request, "state.html")

def about(request):
    return render (request, "about.html")

def contact(request):
    return render (request, "contact.html")

def elements(request):
    return render (request, "elements.html")

def index(request):
    return render (request, "index.html")

def post(request):
    return render (request, "post.html")

def services(request):
    return render (request, "services.html")

def singlePost(request):
    return render (request, "single-post.html")