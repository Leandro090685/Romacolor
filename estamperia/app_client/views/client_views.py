from rest_framework import generics
from app_client.completemodels.client import Client
from app_client.serializers.client_serializer import ClientSerializer

#GET#POST
class ClientCreateReadView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

