from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    return render(request,'index.html')


def about(request):

    return render(request,"about.html")

def project(request):

    return render(request,"project.html")



def certificates(request):

    return render(request,"certificates.html")

def experiences(request):

    return render(request,"experiences.html")