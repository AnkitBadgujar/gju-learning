from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1": "hii my name is ankit",
        "variable2": "hii my name is anii",
        "variable3": "hii my name is neetu"
    }
    
    return render(request, "index.html",context)
    #return HttpResponse("this is homepage")
def about(request):
    return render(request, "about.html")

    #return HttpResponse("this is about page")
def services(request):
    return render(request, "services.html")

    #return HttpResponse("this is sevices page")
def photoshoot(request):
    return render(request, "photoshoot.html")

def wedding(request):
    return render(request, "wedding.html")

def pre_wedding(request):
    return render(request, "pre_wedding.html")
def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        desc=request.POST.get('desc')

        
        contact = Contact(name=name , phone=phone, email=email, password=password, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,"your message has been sent")
    
    return render(request,"contact.html")

    #return HttpResponse("this is contact page")