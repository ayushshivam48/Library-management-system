class Library:
    def __init__(self):
        # Initialize an empty dictionary to store books
        self.books = {}

    def add_book(self, book_name, author, copies):
        """
        Add a new book to the library.
        :param book_name: Name of the book to add
        :param author: Name of the book's author
        :param copies: Number of copies of the book
        """
        self.books[book_name] = {
            "author": author,
            "copies": copies,
            "issued": 0  # Track how many copies have been issued
        }
        print(f"Book '{book_name}' added successfully.")

    def display_books(self):
        """
        Display all the available books in the library.
        """
        print("\nAvailable books:")
        if not self.books:
            print("No books available in the library.")
        for book, details in self.books.items():
            print(f"Title: {book}, Author: {details['author']}, Copies: {details['copies']}, Issued: {details['issued']}")
        print()

    def issue_book(self, book_name):
        """
        Issue a book to a user.
        :param book_name: Name of the book to issue
        """
        # Check if the book exists and there are copies available to issue
        if book_name in self.books and self.books[book_name]['copies'] > self.books[book_name]['issued']:
            self.books[book_name]['issued'] += 1  # Increase the issued count
            print(f"Book '{book_name}' has been issued.")
        else:
            # If book not found or all copies are issued
            print(f"Sorry, the book '{book_name}' is not available or all copies are issued.")

    def return_book(self, book_name):
        """
        Return a previously issued book.
        :param book_name: Name of the book to return
        """
        # Check if the book exists and at least one copy has been issued
        if book_name in self.books and self.books[book_name]['issued'] > 0:
            self.books[book_name]['issued'] -= 1  # Decrease the issued count
            print(f"Book '{book_name}' has been returned.")
        else:
            # If the book was never issued or does not exist in the library
            print(f"Cannot return the book '{book_name}', it was not issued.")

def main():
    # Create an instance of the Library class
    library = Library()

    while True:
        # Menu for the library system
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        # Take user input for the menu option
        choice = input("Enter your choice: ")

        if choice == '1':
            # Option to add a book
            book_name = input("Enter the book name: ")
            author = input("Enter the author name: ")
            copies = int(input("Enter the number of copies: "))
            library.add_book(book_name, author, copies)

        elif choice == '2':
            # Option to display all available books
            library.display_books()

        elif choice == '3':
            # Option to issue a book
            book_name = input("Enter the book name to issue: ")
            library.issue_book(book_name)

        elif choice == '4':
            # Option to return a book
            book_name = input("Enter the book name to return: ")
            library.return_book(book_name)

        elif choice == '5':
            # Exit the program
            print("Exiting the Library Management System.")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select again.")

# Entry point of the program
if __name__ == "__main__":
    main()
