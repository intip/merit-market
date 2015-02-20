from django.core.management.base import BaseCommand
from core.models import Customer


class Command(BaseCommand):
    help = "resets week of hearts"

    def handle(self, *args, **options):
        total = Customer.objects.all().update(weekly_hearts=15)
        self.stdout.write('Total resets "%s"' % total)
