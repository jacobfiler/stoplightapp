import csv
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stoplight.settings")
django.setup()

from stoplight_app.models import Reform, ReformArea

# Path to the CSV file
csv_file_path = '2024-2025slc.csv'

# Function to import data from CSV
def import_reforms_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Normalize headers
        reader.fieldnames = [header.strip('\ufeff').strip() for header in reader.fieldnames]
        
        # Print normalized headers for debugging
        headers = reader.fieldnames
        print("Normalized CSV Headers:", headers)
        
        for row in reader:
            # Get or create the ReformArea
            reform_area, created = ReformArea.objects.get_or_create(name=row['Reform Area'].strip())
            
            # Create the Reform
            reform = Reform(
                slcid=row['SLC ID#'].strip(),
                name=row['Reform'].strip(),
                description=row['Reform Description'].strip() if row['Reform Description'] else None,
                reform_area=reform_area,
                version=2,
                policy_specialist=row['Policy Specialist'].strip() if row['Policy Specialist'] else None
            )
            reform.save()

# Call the function to import data
import_reforms_from_csv(csv_file_path)
