def add(a, b, c=None):
    if c is None:
        if isinstance(a, int) and isinstance(b, int):
            print("The Sum is:", a + b)
        elif isinstance(a, float) and isinstance(b, float):
            print("The Sum is:", a + b)
    else:
        print("The Sum is:", a + b + c)

# Call the add function with different arguments
add(5, 3)       # Sum of two integers
add(2.5, 1.8)   # Sum of two floats
add(1, 2, 3)    # Sum of three integers