class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            # Check if both arguments are integers or floats
            if isinstance(a, int) and isinstance(b, int):
                print("The Sum is:", a + b)
            elif isinstance(a, float) and isinstance(b, float):
                print("The Sum is:", a + b)
        else:
            # Three arguments are provided
            print("The Sum is:", a + b + c)