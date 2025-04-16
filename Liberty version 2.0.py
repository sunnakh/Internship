from datetime import datetime
import os


class Book:
    def __init__(
        self,
        title,
        author,
        year,
        isbn,
        genre,
        is_borrowed=False,
        borrowed_by=None,
        borrowed_date=None,
        borrow_count=0,
    ):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrowed_date = borrowed_date
        self.borrow_count = borrow_count

    def get_summary(self):
        return f"{self.title} by {self.author} ({self.year}) | Genre: {self.genre} | Borrowed: {self.is_borrowed}"

    def mark_borrowed(self, user_id):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user_id
            self.borrowed_date = datetime.now()
            self.borrow_count += 1
        else:
            print("Book is already borrowed.")

    def mark_returned(self):
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None

    def serialize(self):
        date_str = self.borrowed_date.isoformat() if self.borrowed_date else "None"
        return f"{self.title}|{self.author}|{self.year}|{self.isbn}|{self.genre}|{self.is_borrowed}|{self.borrowed_by}|{date_str}|{self.borrow_count}"

    @staticmethod
    def deserialize(line):
        parts = line.strip().split("|")
        borrowed_date = datetime.fromisoformat(parts[7]) if parts[7] != "None" else None
        return Book(
            title=parts[0],
            author=parts[1],
            year=parts[2],
            isbn=parts[3],
            genre=parts[4],
            is_borrowed=(parts[5] == "True"),
            borrowed_by=parts[6] if parts[6] != "None" else None,
            borrowed_date=borrowed_date,
            borrow_count=int(parts[8]),
        )


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
            self.history.append((book, "Borrowed", datetime.now()))
        else:
            print("Book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book)
            self.history.append((book, "Returned", datetime.now()))
        else:
            print("This book was not borrowed by this user.")

    def get_current_borrowed(self):
        return [book.title for book in self.borrowed_books]

    def get_history(self):
        return [
            (entry[0].title, entry[1], entry[2].strftime("%Y-%m-%d %H:%M"))
            for entry in self.history
        ]

    def serialize(self):
        return f"{self.user_id}|{self.username}"

    @staticmethod
    def deserialize(line):
        parts = line.strip().split("|")
        return User(parts[0], parts[1])


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.books_file = "books.txt"
        self.users_file = "users.txt"
        self.load_data()

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = input("Enter year: ")
        isbn = input("Enter ISBN: ")
        genre = input("Enter genre: ")
        book = Book(title, author, year, isbn, genre)
        self.books.append(book)
        print("Book added successfully.")
        self.save_data()

    def register_user(self):
        user_id = input("Enter user ID: ")
        username = input("Enter username: ")
        user = User(user_id, username)
        self.users.append(user)
        print("User registered successfully.")
        self.save_data()

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def search_books(self):
        keyword = input("Enter keyword to search: ")
        results = [
            book.get_summary()
            for book in self.books
            if keyword.lower() in book.title.lower()
            or keyword.lower() in book.author.lower()
            or keyword.lower() in book.genre.lower()
        ]
        if results:
            print("Search Results:")
            for res in results:
                print(res)
        else:
            print("No books found.")

    def borrow_book(self):
        user_id = input("Enter user ID: ")
        isbn = input("Enter book ISBN to borrow: ")
        user = self.get_user_by_id(user_id)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            user.borrow_book(book)
            print(f"{user.username} borrowed '{book.title}'")
            self.save_data()
        else:
            print("User or Book not found.")

    def return_book(self):
        user_id = input("Enter user ID: ")
        isbn = input("Enter book ISBN to return: ")
        user = self.get_user_by_id(user_id)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            user.return_book(book)
            print(f"{user.username} returned '{book.title}'")
            self.save_data()
        else:
            print("User or Book not found.")

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if not book.is_borrowed:
                print(book.get_summary())

    def show_user_borrowed(self):
        user_id = input("Enter user ID: ")
        user = self.get_user_by_id(user_id)
        if user:
            print("Currently Borrowed Books:")
            print(user.get_current_borrowed())
        else:
            print("User not found.")

    def show_user_history(self):
        user_id = input("Enter user ID: ")
        user = self.get_user_by_id(user_id)
        if user:
            print("User Borrow History:")
            for entry in user.get_history():
                print(entry)
        else:
            print("User not found.")

    def generate_statistics(self):
        total_books = len(self.books)
        borrowed_books = sum(1 for book in self.books if book.is_borrowed)
        most_borrowed = sorted(self.books, key=lambda x: x.borrow_count, reverse=True)[
            :3
        ]
        print("📊 Library Stats:")
        print(f"Total Books: {total_books}")
        print(f"Currently Borrowed: {borrowed_books}")
        print("Most Borrowed Books:")
        for book in most_borrowed:
            print(f"{book.title} - Borrowed {book.borrow_count} times")

    def save_data(self):
        with open(self.books_file, "w", encoding="utf-8") as bf:
            for book in self.books:
                bf.write(book.serialize() + "\n")
        with open(self.users_file, "w", encoding="utf-8") as uf:
            for user in self.users:
                uf.write(user.serialize() + "\n")

    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, "r", encoding="utf-8") as bf:
                self.books = [Book.deserialize(line) for line in bf if line.strip()]
        if os.path.exists(self.users_file):
            with open(self.users_file, "r", encoding="utf-8") as uf:
                self.users = [User.deserialize(line) for line in uf if line.strip()]


library = Library()


def show_menu():
    print("\n📚 LIBRARY SYSTEM MENU 📚")
    print("1. Add Book")
    print("2. Register User")
    print("3. Search Books")
    print("4. List Available Books")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Show User Borrowed Books")
    print("8. Show User Borrow History")
    print("9. Show Library Statistics")
    print("0. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_user()
    elif choice == "3":
        library.search_books()
    elif choice == "4":
        library.list_available_books()
    elif choice == "5":
        library.borrow_book()
    elif choice == "6":
        library.return_book()
    elif choice == "7":
        library.show_user_borrowed()
    elif choice == "8":
        library.show_user_history()
    elif choice == "9":
        library.generate_statistics()
    elif choice == "0":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
