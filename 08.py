# Get user input for the name
a = input("Enter Your Name: ")

# Initialize count
count = 0

# Calculate the length of the string
for char in a:
    count += 1

# Print the name and its length
print("Name:", a)
print("Length:", count)