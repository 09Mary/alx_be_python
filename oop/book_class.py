class Book:
    def __init__(self, title, author, year):
        """Constructor: initializes the Book object with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
