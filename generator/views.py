from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def eggs(request):
    return HttpResponse("Eggs are so tasty")
def rendering(request):
    return render(request,'generator/home.html')
def password(request):
    thestring=""
    Characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("uppercase"):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("special"):
        Characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get("number"):
        Characters.extend(list('1234567890'))

    length=int(request.GET.get("length",12))
    for x in range(length):
        thestring += random.choice(Characters)

    return render(request,'generator/password.html',{"password":thestring})
def about(request):
    return render(request,'generator/about.html')
