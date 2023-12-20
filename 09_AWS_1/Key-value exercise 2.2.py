# Exercise 2.2

import csv

# Create a dictionary to store the user's information
user_info = {}

# Prompt the user for their information
print("Please enter your information (first name, last name, job title, company):")
user_info['First Name'] = input()
user_info['Last Name'] = input()
user_info['Job Title'] = input()
user_info['Company'] = input()

# Open a CSV file in append mode to add new data without overwriting existing data
with open('user_information.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=user_info.keys())

    # Write the user's information to the CSV file
    writer.writerow(user_info)

print("Your information has been saved to the CSV file: user_information.csv")
