user_info = {}

print("Please enter your first name:")
user_first_name = input()

print("Please enter your last name:")
user_last_name = input()

print("Please enter your job title:")
user_job_title = input()

print("Please enter your company name:")
user_company = input()

user_info['First Name'] = user_first_name
user_info['Last Name'] = user_last_name
user_info['Job Title'] = user_job_title
user_info['Company'] = user_company

print("Your information is saved in the dictionary:")
print(user_info)
