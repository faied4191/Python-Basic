# Define the function to calculate the sum
def is_sum(x, y):
    return x + y

# Define the function to find the maximum of two numbers
def is_max(x, y):
    if x > y:
        return x
    else:
        return y

# Get user input for two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Calculate the sum and maximum using the functions
sum_result = is_sum(a, b)
max_result = is_max(a, b)

# Print the results
print("The sum is:", sum_result)
print("The maximum number is:", max_result)