from rest_framework import generics,status
from app_client.completemodels.movements import Movements
from app_client.serializers.movement_serializer import MovementSerializer 

from rest_framework.response import Response 


class MovementsListview(generics.ListAPIView):
    serializer_class = MovementSerializer
    
    def get_queryset(self, *args, **kwargs):
        name = self.kwargs.get('name')
        queryset = Movements.objects.filter(client=name)
        return queryset