# Get the number of elements from the user
a = int(input("Enter the number of elements: "))

# Initialize an empty list
arr1 = []

# Populate the list with user input
for i in range(a):
    element = input(f"Enter element name {i + 1}: ")
    arr1.append(element)

# Print the elements and their values
print("\nElements and values:")
for i in range(a):
    print(f"arr1[{i}] = {arr1[i]}")