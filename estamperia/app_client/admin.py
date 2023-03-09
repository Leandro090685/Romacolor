from django.contrib import admin
from app_client.models import Client, Movements

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Movements)
class MovementsAdmin(admin.ModelAdmin):
    pass



