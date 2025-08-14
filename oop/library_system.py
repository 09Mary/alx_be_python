class Book:
    def __init__(self, title, author):
        """Base class for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for base Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook class inherits from Book and adds file_size."""
        super().__init__(title, author)  
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """PrintBook class inherits from Book and adds page_count."""
        super().__init__(title, author)  
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library stores a collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)  
