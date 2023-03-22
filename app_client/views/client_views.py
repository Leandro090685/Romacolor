from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from app_client.completemodels.client import Client
from app_client.serializers.client_serializer import ClientSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    


