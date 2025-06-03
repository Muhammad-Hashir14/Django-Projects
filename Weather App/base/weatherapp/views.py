from django.shortcuts import render, HttpResponse
import json
import requests
from django.conf import settings
import dotenv

# Create your views here.
def home(request):
    if request.method == "POST":
            city = request.POST["city"]
            apikey = settings.OPENWEATHER_API_KEY
            print(apikey)
            source = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={apikey}"
            try:
                data = requests.get(source).json()

                info = {
                    "country" : str(data['sys']['country']),
                    "cordinates" : str(data['coord']['lon']) + ' ' + str(data["coord"]["lat"]),
                    "temperature" : round(5/9 * (data["main"]["temp"] - 32), 2),
                    "humidity" : str(data["main"]["humidity"]),
                }
            except:
                info = {"country": "Error"}
            
            
    else:
        info = {}
      
    
    return render(request, "home.html", info)