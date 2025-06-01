from django.shortcuts import render, HttpResponse   
import random
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def passwordgen(request):
    string = "qwertyuioplkjhgfdsazxcvbnm"
    if request.GET.get("uppercase"):
        string += "QWERTYUIOPASDFGHJKLZXCVBNM"
    if request.GET.get("digits"):
        string+= "1234567890"
    if request.GET.get("characters"):
        string+="@!#$%^&?"
    length = int(request.GET.get("length", 10))
    password = ""
    for i in range(length):
        chrc = random.choice(string)
        password+=chrc
    return render(request, "password.html", {"password" : password})