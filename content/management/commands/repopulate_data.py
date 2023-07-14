from django.core.management.base import BaseCommand, CommandError
from content.models import Games
from utility.data.data_entry import start_refresh_if_needed
from utility.data.data_update import replace_old_data


class Command(BaseCommand):
    help = "checks if data needs repopulated based on the timestamp utility app"
    
    def add_arguments(self, parser):
        # Force refresh arg
        parser.add_argument(
            "--FORCE",
            action="store_true",
            help="Repopulate data even if recently done",
        )

    def handle(self, *args, **options):
        if not start_refresh_if_needed() and not options['FORCE']:
            self.stdout.write(
                self.style.NOTICE(
                    "Data not repopulated due to recency of previous update"
                )
            )
        else:
            
            self.stdout.write(
                self.style.SUCCESS(
                    "Data successfully refilled."
                )
            )
            replace_old_data()
            self.stdout.write(
                self.style.SUCCESS(
                    "Old Data successfully replaced."
                )
            )
            
