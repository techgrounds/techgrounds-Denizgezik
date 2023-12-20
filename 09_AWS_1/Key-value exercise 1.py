person = {
    'First Name': 'Casper',
    'Last Name': 'Velzen',
    'Job Title': 'Learning Coach',
    'Company': 'Techgrounds'
}

for key, value in person.items():
    print(f"{key}: {value}")


# another example:

# Create a dictionary with keys and values.
employee_info = {
    "First name": "Casper",
    "Last name": "Velzen",
    "Job title": "Learning coach",
    "Company": "Techgrounds"
}

# Loop over the dictionary and print every key-value pair.
print("Employee Information:")
for key, value in employee_info.items():
    print("{}: {}".format(key, value))
