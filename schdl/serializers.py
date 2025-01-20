from rest_framework import serializers
from .models import BHP,LHP

class BHPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BHP
        fields = ['img']

class LHPSerializer(serializers.ModelSerializer):
    class Meta:
        model = LHP
        fields = ['img']
