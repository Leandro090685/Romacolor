from app_client.completemodels.movements import Movements
from app_client.serializers.movement_serializer import MovementSerializer 
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView



class MovementListView(generics.ListAPIView):
    queryset = Movements.objects.all()
    serializer_class = MovementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name__name','type',]

class MovementTotalListView(APIView):
    def get(self,request,name,*args, **kwargs):
        query = Movements.objects.filter(name__name = name)
        response = query.aggregate(suma=Sum("amount"))
        return Response(response)
    
class CuentaCorriente(APIView):
    def get(self,request,name):
        name = self.kwargs['name']
        queryset = Movements.objects.filter(name__name = name)
        serializer = MovementSerializer(queryset, many = True)
        return Response (serializer.data)
        

