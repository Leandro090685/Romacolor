from rest_framework import serializers
from app_client.completemodels.movements import Movements
from rest_framework.fields import CharField

class MovementSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Movements
        fields = ("client", "date", "type", "description", "quantity", "amount")
        
    
    