import random

# Initialize an empty list
random_numbers = []

# Generate 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Print the original list
print("Original list:", random_numbers)

# Remove odd numbers and replace even numbers with their double value
filtered_numbers = []  # Create a new list to store modified values
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        filtered_numbers.append(num * 2)  # Double the even number

# Print the final modified list
print("Modified list:", filtered_numbers)