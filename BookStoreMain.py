from pickle import TRUE


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
            print(f"Warning: You have {self.items[book]} of {book.title} in your card, but only {book.stock} are available in the stock")


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
    def  __init__(self, username, initial_balance = 0):
        self.username = username
        self.card = Card()
        self.initial_balance = initial_balance
            
    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            return TRUE
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
        for  book in self.books:
            print(book)
            
    def  checkout(self, user):
        total_price = user.card.get_total_price()
        
        if user.initial_balance >= total_price:
            user.initial_balance -= total_price
            for book, quantity in user.card.items.items():
                book.stock -= quantity
            print("Purchased successfully! Your new balance is {user.initial_balance}.")
        else:
            print(f"Insufficient balance. You need {total_price - user.initial_balance} more to purchase.")
            
# Example usage

if __name__ == "__main__":
    bookstore = Store()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99, 5)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 14.99, 3)
    book3 = Book("1984", "George Orwell", 11.99, 7)

    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)
    
    # Creating user
    user = User("Sunnakh", 50.0)
    
    # List of all books
    print("Avaliable books: ")
    bookstore.list_books()
    print()
    
    # Search for a book
    
    print("Search results for 'the': ")
    for book in bookstore.search_by_title("the"):
        print(book)
    print()
    
    # Add books to the card
    
    user.card.add_to_card(book=book1, quantity= 3)
    user.card.add_to_card(book=book3, quantity= 1)
    
    # Get total Price
    print(f"Card total: {user.card.get_total_price():.2f}")
    
    # process checkout
    bookstore.checkout(user)
    
    # show updated stock
    print("Updated book inventory: ")
    bookstore.list_books()
        
        
