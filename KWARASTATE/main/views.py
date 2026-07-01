from django.shortcuts import render,redirect
from .models import ContactMessage

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render (request, "about.html")

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone')
        service_of_interest = request.POST.get('service')
        message = request.POST.get('message')

        # save to database 
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            phone_no=phone_no,
            service_of_interest=service_of_interest,
            message=message
        )

        # send notification to mail
        send_mail(
                  subject=f"{full_name},New contact messsage from kwara website",
                  message=f"""
 Name:{full_name}
 Email:{email}
                 
 Message:{message}
""" ,
from_email= settings.DEFAULT_FROM_EMAIL,
recipient_list=["abdulkareemjamal50@gmail.com"],
fail_silently=False,
)
        messages.success(request, "Message sent successfully") 
        return redirect('contact')            

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