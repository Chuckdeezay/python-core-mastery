class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"
    
    def __eq__(self, other):
        return self.pages == other.pages

    def __len__(self):
        return self.pages

b = Book("Python Deep Dive", 350)

print(b)
print(repr(b))

b1 = Book("Book A", 300)
b2 = Book("Book B", 300)

print(b1 == b2)

print(len(b1))