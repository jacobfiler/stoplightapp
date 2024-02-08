from django.core.management.base import BaseCommand
from stoplight_app.models import State

class Command(BaseCommand):
    help = 'Imports a list of all 50 US states into the database'

    def handle(self, *args, **kwargs):
        states_list = [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California",
            "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
            "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
            "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
            "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
            "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
            "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
            "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
            "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
            "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        ]

        for state_name in states_list:
            State.objects.get_or_create(name=state_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created state "{state_name}"'))
