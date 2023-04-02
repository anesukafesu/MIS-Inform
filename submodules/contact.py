#!/usr/bin/python3
# Define the contact information as a list of dictionaries
contacts = [
    {
        "name": "Ministry of Finance and Economic Planning",
        "website": "minecofin.gov.rw",
        "email": "info@minecofin.gov.rw",
        "tel": "+250 252 577 581",
        "physical_address": "12 KN3 Ave, Kigali"
    },
    {
        "name": "Ministry of Health",
        "website": "rbc.gov.rw",
        "email": "info@rbc.gov.rw",
        "tel": "+250 788 200 049",
        "physical_address": "KG 9 Ave, Kigali"
    },
    {
        "name": "Rwanda Development Board",
        "website": "rdb.rw",
        "email": "info@rdb.rw",
        "tel": "+250 252 580 222",
        "physical_address": "Gishushu, KG 9 Ave, Kigali"
    },
    {
        "name": "Rwanda National Police",
        "website": "police.gov.rw",
        "email": "info@police.gov.rw",
        "tel": "+250 788 311 155",
        "physical_address": "KN 5 Rd, Kacyiru, Kigali"
    },
    {
        "name": "Rwanda Immigration Department",
        "website": "immigration.gov.rw",
        "email": "info@migration.gov.rw",
        "tel": "+250 78 815 2222",
        "physical_address": "Kimihurura, KG 9 Ave, Kigali"
    }
]

# Define the emergency numbers as a dictionary
emergency_numbers = {
    "Ambulance": "912",
    "Fire Department": "112",
    "Police": "112 or 999"
}

# Display the contact information
print("Key Government Department Contacts:")
for contact in contacts:
    print(f"\nName: {contact['name']}")
    print(f"Website: {contact['website']}")
    print(f"Email: {contact['email']}")
    print(f"Telephone: {contact['tel']}")
    print(f"Physical Address: {contact['physical_address']}")

# Display the emergency numbers
print("\nEmergency Numbers in Rwanda:")
for name, number in emergency_numbers.items():
    print(f"\n{name}: {number}")

