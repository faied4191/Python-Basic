class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)

# Create instances of Book
ob1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
ob2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)