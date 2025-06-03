from django.shortcuts import render, HttpResponse
import json
import requests

# Create your views here.
def home(request):
    if request.method == "POST":
            city = request.POST["city"]
            source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c40a10a2a476d5cc919e7096cc4e2c39"
            try:
                data = requests.get(source.format(city)).json()

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