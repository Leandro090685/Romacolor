from django.db import models


class Client(models.Model):
  name = models.CharField(max_length=128, unique = True)

  def __str__(self) -> str:
    return self.name


    

