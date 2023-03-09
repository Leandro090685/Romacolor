from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
      return f"{self.name}" 

