# Get the number of elements from the user
a = int(input("Enter the number of elements: "))

# Initialize an empty list
arr1 = []

# Populate the list with user input
for i in range(a):
    element = input(f"Enter element name {i + 1}: ")
    arr1.append(element)

# Print the first element and its length
print("First Element Name:", arr1[0])
print("First Element Size:", len(arr1[0]))

# Print the size of the list
print("Array Size:", len(arr1))