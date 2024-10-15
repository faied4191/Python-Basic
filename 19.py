class Adder:
    def __init__(self, i=0):
        self.total = i

    def add_num(self, number):
        self.total += number

    def get_total(self):
        return self.total

# Create an instance of Adder
a = Adder()

# Add numbers
a.add_num(10)
a.add_num(20)
a.add_num(30)

# Print the total
print("Total", a.get_total())