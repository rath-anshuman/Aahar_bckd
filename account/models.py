from django.db import models

class Visitor(models.Model):
    day=models.DateField(unique=True)
    count=models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return f"{self.day} - {self.count}"
    



    
from rest_framework import serializers

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['day','count']
