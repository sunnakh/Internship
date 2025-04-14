from datetime import datetime
class Book:
    def __init__(self, title, author, year, isbn, genre):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = datetime.now()
        self.borrow_count = 0
        
    
    def get_summary(self):
        return f"{self.title} by {self.author} ({self.year} - Genre: {self.genre} | Borrowed: {self.is_borrowed})"
    
    def mark_borrowed(self, user_id):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user_id
            self.borrowed_date = datetime.now()
            self.borrow_count += 1
        else:
            print("Book is already borrowed")
            
    def mark_returned(self):
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None 

class User:
    
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.borrowed_books = []
        self.history = []
        
    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_borrowed(self.user_id)
            self.borrowed_books.append(book)
            self.history.append(book, "Borrowed", datetime.now())
        else:
            print("Book is already borrowed")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book)
            self.history.append(book, "Returned", datetime.now())
        else:
            print("This book was not borrowed by this user.")
            
    def get_current_borrowed(self):
        return [book.title for  book in self.borrowed_books]

    def get_history(self):
        return [(entry[0].title, entry[1], entry[2].strftime('%Y-%m-%d %H:%M')) for entry in self.history]
    
class Library:
    
    def __init__(self, books, users):
        self.books = books
        self.users = users
    
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def search_books(self, keyword):
        return [book.get_summary() for book in self.books
                if keyword.lower() in book.title.lower() or
                   keyword.lower() in book.author.lower() or
                   keyword.lower() in book.genre.lower()]

    def list_available_books(self):
        return [book.get_summary() for book in self.books if not book.is_borrowed]

    def register_user(self, user):
        self.users.append(user)

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
            else:
                print("User not found")
        return None

    def borrow_book(self, user_id, isbn):
        user = self.get_user_by_id(user_id)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            user.borrow_book(book)
        else:
            print("User or book not found.")

    def return_book(self, user_id, isbn):
        user = self.get_user_by_id(user_id)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            user.return_book(book)
        else:
            print("User or book not found.")

    def generate_statistics(self):
        total_books = len(self.books)
        borrowed_books = sum(1 for book in self.books if book.is_borrowed)
        most_borrowed = sorted(self.books, key=lambda x: x.borrow_count, reverse=True)[:3]
        return {
            "total_books": total_books,
            "borrowed_books": borrowed_books,
            "most_borrowed_books": [(book.title, book.borrow_count) for book in most_borrowed]
        }  