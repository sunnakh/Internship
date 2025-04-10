from pickle import TRUE
from turtle import title


class Book:
    next_id = 1

    def __init__(self, title, author, price, stock):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Price: {self.price:.2f}, Stock: {self.stock}."


class Card:
    def __init__(self):
        self.items = {}

    def add_to_card(self, book, quantity):
        if book in self.items:
            self.items[book] += quantity
        else:
            self.items[book] = quantity

        if self.items[book] > book.stock:
            print(
                f"Warning: You have {self.items[book]} of {book.title} in your card, but only {book.stock} are available in the stock")

    def remove_from_card(self, book):
        if book in self.items:
            del self.items[book]
            print(f"{book.title} has removed successfully.")

    def get_total_price(self):
        total = 0
        for book, quantity in self.items.items():
            total += book.price * quantity
        return total


class User:
    def __init__(self, username, initial_balance=0):
        self.username = username
        self.card = Card()
        self.balance = initial_balance

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            return True  
        return False


class Store:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results  


    def list_books(self):
        for book in self.books:
            print(book)

    def checkout(self, user):
        total_price = user.card.get_total_price()

        if user.balance >= total_price:
            user.balance -= total_price

            for book, quantity in user.card.items.items():
                book.stock -= quantity
            print(f"Purchased successfully! Your new balance is {user.balance}.")
        else:
            print(f"Insufficient balance. You need {total_price - user.balance} more to purchase.")



# Example usage

if __name__ == "__main__":
    bookstore = Store()
    book_cycle = int(input("Enter how many books do you want to enter: "))
    username = str(input("Enter your username: "))
    balance = float(input("Enter your initial balance: "))
    
    while book_cycle > 0:
        book_title = input("\nEnter the book title: ")
        book_author = input("Enter the book author: ")
        book_price = float(input("Enter the book price: "))
        book_stock = int(input("Enter the book stock: "))
        
        book = Book(book_title, book_author, book_price, book_stock)
        bookstore.add_book(book)  
        
        book_cycle -= 1  

    # creating user
    user = User(username= username, initial_balance= balance)
    
    # list of all books
    print("Available books: ")
    print()
    bookstore.list_books()
    print()
    
    # search for a book
    
    search_title = str(input("Enter book's title to search: "))
    
    found_books = bookstore.search_by_title(search_title)
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(book)
    else:
        print("No books found with that title.")


    
    # add books to the card:
    
    book_titles_to_add = int(input("\nHow many different books do you want to add to the card: "))
    
    for _ in range(book_titles_to_add):
        book_title = str(input("\nEnter a book title to add the card: "))
        book_quantity = int(input("Enter the quantity of the book: "))
        
        found_books = bookstore.search_by_title(book_title)
        if not found_books:
            print(f"Book {book_title} not found in the store.")
            continue
        else:
            for book in found_books:
                print(book)

            
        book = found_books[0]
        
        if book.stock > book_quantity:
            user.card.add_to_card(book, book_quantity)
            print(f"Added {book_quantity} of {book_title} to the card.")
        else:
            print(f"Not enough stock for {book_title}. Available stock: {book.stock}")
    
    
    #  get total price
    total_price = user.card.get_total_price()
    print(f"\nCard total: {total_price:.2f}")
    
    #  process checkout
    bookstore.checkout(user)
    
    # show updated stock
    print("\nUpdated book inventory: ")
    print()
    bookstore.list_books()
            
    
        
    
        
        
