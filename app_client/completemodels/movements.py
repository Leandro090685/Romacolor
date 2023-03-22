from django.db import models
from app_client.models import Client

class MovementType(models.TextChoices):
    PAGO = "PAGO"
    INGRESO = "INGRESO"


class Movements(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)
    type = models.TextField(choices=MovementType.choices, blank=False)
    description = models.TextField(max_length=128)
    quantity = models.PositiveIntegerField()
    amount = models.FloatField()

    def __str__(self) -> str:
        return f"{self.client} {self.type}"
