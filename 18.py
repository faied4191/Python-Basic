def add(a, b, c=None):
    if c is None:
        if isinstance(a, int) and isinstance(b, int):
            print("The Sum is:", a + b)
        elif isinstance(a, float) and isinstance(b, float):
            print("The Sum is:", a + b)
    else:
        print("The Sum is:", a + b + c)