from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mtlogin(request):
    return render(request,'mt login.html')

def mtsignup(request):
    return render(request,'mt signup.html')

def mthome(request):
    return render(request,'mt home.html')
