from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherEntitySerializer

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        return render(request, "home.html", {"weathers":weathers})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        temperature = randrange(start=17, stop=40)
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        city = "Sorocaba"  
        atmosphericPressure = randrange(start=900, stop=1100)

        weather_data = {
            "temperature": temperature,
            "date": date,
            "city": city,
            "atmosphericPressure": atmosphericPressure,
        }
        serializer = WeatherEntitySerializer(data=weather_data)
        if serializer.is_valid():
            repository.insert(serializer.validated_data)
        return redirect('Weather View')
    
class WeatherReset(View):
    def get(self, request):
        repository = WeatherRepository(collectionName="weathers")
        repository.deleteAll()

        return redirect('Weather View')