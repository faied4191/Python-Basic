# Get user input for three numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# Determine the greatest number
if a > b and a > c:
    greatest = a
elif b > a and b > c:
    greatest = b
else:
    greatest = c

# Print the greatest number
print("The Greatest is:", greatest)