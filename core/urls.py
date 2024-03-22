from django.urls import path
from weather.views import WeatherView
from weather.views import WeatherGenerate
from weather.views import WeatherReset

urlpatterns = [
    path('', WeatherView.as_view(), name="Weather View"),
    path ('generate', WeatherGenerate.as_view(), name="WeatherGenerate"),
    path ('reset', WeatherReset.as_view(), name="WeatherReset"),
]
