from django.urls import path
from app_client.views.client_views import ClientListView
from app_client.views.movement_views import MovementListView, MovementTotalListView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name= "clients"),
    path('movements/', MovementListView.as_view(), name= 'movements'),
    path('movements/total/<name>', MovementTotalListView.as_view(), name= 'total')

]



