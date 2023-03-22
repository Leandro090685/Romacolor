from rest_framework import serializers
from app_client.completemodels.client import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        