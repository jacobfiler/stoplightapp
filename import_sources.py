import os
import django
import csv

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stoplight.settings')
django.setup()

from stoplight_app.models import Reform, State, ReformStatus, Source, SourceType

# Load or create State instances
def get_or_create_state(name):
    state, created = State.objects.get_or_create(name=name)
    print(f"State: {state.name} (Created: {created})")
    return state

# Load or create SourceType instances
def get_or_create_source_type(name):
    source_type, created = SourceType.objects.get_or_create(name=name)
    print(f"SourceType: {source_type.name} (Created: {created})")
    return source_type

# Define the path to your CSV file
csv_file_path = 'combined_data.csv'

# Open the CSV file and read its contents
with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Processing row: {row}")
        
        # Get the Reform instance
        slcid = row.get('SLC ID#')
        if not slcid:
            print("No SLC ID found in row, skipping.")
            continue
        
        try:
            reform = Reform.objects.get(slcid=slcid)
        except Reform.DoesNotExist:
            print(f"Reform with SLC ID {slcid} does not exist.")
            continue

        # Get or create the State instance
        state_name = row.get('State')
        state = get_or_create_state(state_name)

        # Extract additional notes
        additional_notes = row.get('Additional Notes')
        print(f"Additional Notes for SLC ID {slcid} in {state_name}: {additional_notes}")

        # Create or update the ReformStatus instance
        reform_status, created = ReformStatus.objects.update_or_create(
            reform=reform,
            state=state,
            defaults={
                'additional_notes': additional_notes
            }
        )
        print(f"Updated ReformStatus for SLC ID {slcid} in {state_name}.")

        # Create the first Source instance
        source_1_url = row.get('Source 1')
        source_1_type = row.get('Source Type 1')
        if source_1_url and source_1_type:
            source_type_1 = get_or_create_source_type(source_1_type)
            source_1, created = Source.objects.update_or_create(
                reform_status=reform_status,
                source_type=source_type_1,
                defaults={'url': source_1_url}
            )
            print(f"Source 1 for ReformStatus {reform_status.id}: URL={source_1_url}, Type={source_1_type} (Created: {created})")

        # Create the second Source instance
        source_2_url = row.get('Source 2')
        source_2_type = row.get('Source Type 2')
        if source_2_url and source_2_type:
            source_type_2 = get_or_create_source_type(source_2_type)
            source_2, created = Source.objects.update_or_create(
                reform_status=reform_status,
                source_type=source_type_2,
                defaults={'url': source_2_url}
            )
            print(f"Source 2 for ReformStatus {reform_status.id}: URL={source_2_url}, Type={source_2_type} (Created: {created})")

print("Data import complete.")
