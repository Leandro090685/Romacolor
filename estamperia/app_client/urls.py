from django.urls import path
from app_client.views.client_views import ClientCreateReadView
from app_client.views.movement_views import MovementsListview

urlpatterns = [
   path("clients", ClientCreateReadView.as_view(), name="client-list-create"),
   path("movements/<str:name>", MovementsListview.as_view(), name= "movements-client"),
]
