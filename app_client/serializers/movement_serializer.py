from rest_framework import serializers
from app_client.completemodels.movements import Movements

class MovementSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta: 
        model = Movements
        fields = "__all__"
        
    
    