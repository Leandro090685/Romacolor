from django.apps import AppConfig


class AppClientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_client"

    def ready(self) -> None:
        from app_client.completemodels.client import Client
        from app_client.completemodels.movements import Movements
        return super().ready()
    