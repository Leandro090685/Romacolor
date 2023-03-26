from rest_framework.views import APIView
from app_client.completemodels.movements import Movements
from app_client.serializers.movement_serializer import MovementSerializer
from rest_framework.response import Response


class CuentaCorriente(APIView):
    def get(self,request,name):
        name = self.kwargs['name']
        queryset = Movements.objects.filter(name__name = name)
        serializer = MovementSerializer(queryset, many = True)
        return Response (serializer.data)