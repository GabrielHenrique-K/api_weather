# serializers.py
from rest_framework import serializers
from .models import WeatherEntity

class WeatherEntitySerializer(serializers.Serializer):
    temperature = serializers.IntegerField()
    date = serializers.CharField()
    city = serializers.CharField(required=False)  
    atmosphericPressure = serializers.CharField() 
    humidity = serializers.CharField(required=False)  
    weather = serializers.CharField(required=False) 

    def create(self, validated_data):
        return WeatherEntity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.date = validated_data.get('date', instance.date)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.save()
        return instance
