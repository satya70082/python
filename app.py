# Simple Python program to calculate birth year

# Prompt the user for their name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Get the current year
from datetime import datetime
current_year = datetime.now().year

# Calculate the year of birth
birth_year = current_year - age

# Display the result
print(f"Hello, {name}! You were born in {birth_year}.")
