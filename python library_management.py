class Lib:
    def __init__(self):
        self.books = {}  

    def add_book(self, book_name, quantity):
        self.books[book_name] = self.books.get(book_name, 0) + quantity
        print(f"'{book_name}' added successfully. Quantity: {self.books[book_name]}")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for book_name, quantity in self.books.items():
                print(f"{book_name} (Quantity: {quantity})")

    def issue_book(self, book_name):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            print(f"'{book_name}' has been issued.")
            if self.books[book_name] == 0:
                print(f"Note: '{book_name}' is now out of stock.")
        else:
            print(f"'{book_name}' is not available or out of stock.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
            print(f"'{book_name}' returned successfully.")
        else:
            self.books[book_name] = 1
            print(f"'{book_name}' added to the library.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            book_name = input("Enter book name: ")
            quantity = int(input("Enter quantity: "))
            library.add_book(book_name, quantity)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            book_name = input("Enter book name to issue: ")
            library.issue_book(book_name)
        elif choice == "4":
            book_name = input("Enter book name to return: ")
            library.return_book(book_name)
        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 