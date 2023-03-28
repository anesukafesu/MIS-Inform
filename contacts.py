# Create a dictionary of government departments and their contact information
departments = {
    "Department of Education": {
        "Phone": "555-1234",
        "Email": "education@govt.gov"
    },
    "Department of Health": {
        "Phone": "555-5678",
        "Email": "health@govt.gov"
    },
    "Department of Transportation": {
        "Phone": "555-9012",
        "Email": "transportation@govt.gov"
    }
}

# Define a function to display the government departments and their contact information
def display_government_departments():
    print("Government Departments:")
    for name, info in departments.items():
        print(f"\n{name}\nPhone: {info['Phone']}\nEmail: {info['Email']}")

# Call the function to display the government departments and their contact information
display_government_departments()