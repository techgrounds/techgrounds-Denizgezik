# Extra Exercise 2.2

# Use user input to ask for information.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
job_title = input("Enter your job title: ")
company = input("Enter your company: ")

# Store the information in a dictionary.
user_info = {
    "First name": first_name,
    "Last name": last_name,
    "Job title": job_title,
    "Company": company
}

# Print the user information.
print("\nUser Information:")
for key, value in user_info.items():
    print("{}: {}".format(key, value))

