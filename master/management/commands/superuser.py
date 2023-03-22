from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        user = get_user_model()
        user.objects.create_superuser('leandro', 'admin@admin.com', '1234')

        