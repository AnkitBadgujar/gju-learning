from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def cse1st(request):
    return render(request, "cse1st.html")

def cse2nd(request):
    return render(request, "cse2nd.html")

def cse3rd(request):
    return render(request, "cse3rd.html")

def cse4th(request):
    return render(request, "cse4th.html")

def cse5th(request):
    return render(request, "cse5th.html")

def cse6th(request):
    return render(request, "cse6th.html")

def cse7th(request):
    return render(request, "cse7th.html")

def cse8th(request):
    return render(request, "cse8th.html")

def cse1q(request):
    return render(request, "cse1q.html")

def cse2q(request):
    return render(request, "cse2q.html")

def cse3q(request):
    return render(request, "cse3q.html")

def cse4q(request):
    return render(request, "cse4q.html")

def cse5q(request):
    return render(request, "cse5q.html")

def cse6q(request):
    return render(request, "cse6q.html")

def cse7q(request):
    return render(request, "cse7q.html")

def cse8q(request):
    return render(request, "cse8q.html")

def it1st(request):
    return render(request, "it1st.html")

def it2nd(request):
    return render(request, "it2nd.html")

def it3rd(request):
    return render(request, "it3rd.html")

def it4th(request):
    return render(request, "it4th.html")

def it5th(request):
    return render(request, "it5th.html")

def it6th(request):
    return render(request, "it6th.html")

def it7th(request):
    return render(request, "it7th.html")

def it8th(request):
    return render(request, "it8th.html")

def it1q(request):
    return render(request, "it1q.html")

def it2q(request):
    return render(request, "it2q.html")

def it3q(request):
    return render(request, "it3q.html")

def it4q(request):
    return render(request, "it4q.html")

def it5q(request):
    return render(request, "it5q.html")

def it6q(request):
    return render(request, "it6q.html")

def it7q(request):
    return render(request, "it7q.html")

def it8q(request):
    return render(request, "it8q.html")

def acaque(request):
    return render(request, "aca.html")

def dwdmque(request):
    return render(request, "dwdm.html")

def spmque(request):
    return render(request, "spm.html")

def wmcque(request):
    return render(request, "wmc.html")

def cdque(request):
    return render(request, "cd.html")

def cdls(request):
    return render(request, "cdls.html")

def m3que(request):
    return render(request, "math3.html")

def dsque(request):
    return render(request, "dsque.html")

def oopsque(request):
    return render(request, "c++que.html")

def deque(request):
    return render(request, "deque.html")

def cnque(request):
    return render(request, "cnque.html")

def javaque(request):
    return render(request, "javaque.html")

def dbmsque(request):
    return render(request, "dbmsque.html")

def seque(request):
    return render(request, "seque.html")

def caoque(request):
    return render(request, "caoque.html")

def fmque(request):
    return render(request, "fmque.html")

def pdque(request):
    return render(request, "pdque.html")

def dbmsls(request):
    return render(request, "dbmsls.html")

def cnls(request):
    return render(request, "cnls.html")

def javals(request):
    return render(request, "javals.html")

def osls(request):
    return render(request, "osls.html")

def mpls(request):
    return render(request, "mpls.html")

def wdls(request):
    return render(request, "wdls.html")

def netls(request):
    return render(request, ".netls.html")

def osque(request):
    return render(request, "osque.html")

def mpque(request):
    return render(request, "mpque.html")

def hsnque(request):
    return render(request, "hsnque.html")

def netque(request):
    return render(request, ".netque.html")

def wdque(request):
    return render(request, "wdque.html")

def cgls(request):
    return render(request, "cgls.html")

def isls(request):
    return render(request, "isls.html")

def apls(request):
    return render(request, "apls.html")

def pythonls(request):
    return render(request, "pythonls.html")

def cgque(request):
    return render(request, "cgque.html")

def apque(request):
    return render(request, "apque.html")

def adaque(request):
    return render(request, "adaque.html")

def tocque(request):
    return render(request, "tocque.html")

def isque(request):
    return render(request, "isque.html")

def dmdwview(request):
    return render(request, "dmdwview.html")


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