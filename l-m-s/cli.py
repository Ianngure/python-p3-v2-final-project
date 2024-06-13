from book_operations import add_book, view_books, delete_book, find_book, borrow_book, return_book
from tabulate import tabulate

def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Find Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
            print("Book added successfully.")
        elif choice == '2':
            books = view_books()
            print(tabulate([[book.id, book.title, book.author, "Available" if book.available else "Borrowed"] for book in books], headers=["ID", "Title", "Author", "Status"]))
        elif choice == '3':
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
            print("Book deleted successfully.")
        elif choice == '4':
            title = input("Enter book title to find: ")
            books = find_book(title)
            if books:
                print(tabulate([[book.id, book.title, book.author, "Available" if book.available else "Borrowed"] for book in books], headers=["ID", "Title", "Author", "Status"]))
            else:
                print("No books found with that title.")
        elif choice == '5':
            book_id = input("Enter book ID to borrow: ")
            borrower = input("Enter borrower's name: ")
            borrow_book(book_id, borrower)
            print("Book borrowed successfully.")
        elif choice == '6':
            book_id = input("Enter book ID to return: ")
            return_book(book_id)
            print("Book returned successfully.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
