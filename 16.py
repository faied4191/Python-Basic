class Animal:
    def eat(self):
        print("Eat")

    def sleep(self):
        print("Sleep")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Create an instance of Dog
ob = Dog()