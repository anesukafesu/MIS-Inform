import project

# Define a function to display project information
def display_project_info(p):
    print(f"Project Name: {p.name}")
    print(f"Description: {p.description}")
    print(f"Start Date: {p.start_date}")
    print(f"Estimated Completion Date: {p.estimated_completion_date}")
    print(f"Completion Rate: {p.completion_rate}%")
    print()

# Get a list of all ongoing government projects
projects = project.get_ongoing_government_projects()

# Display information about each project
for p in projects:
    display_project_info(p)
