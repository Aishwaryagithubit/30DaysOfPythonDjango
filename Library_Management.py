# Library Management System 
import random
from datetime import datetime, timedelta

# Base Class 
class Book:
    def __init__(self, title, author):
        self.book_id = str(random.randint(1000, 99999))  
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} — {status}"

# Child Class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"[E-Book {self.book_id}] {self.title} by {self.author} ({self.file_size}MB)"

# Member Class 
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, Books Borrowed: {len(self.borrowed_books)}"

# Library Class 
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add books and members
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully! ID: {book.book_id}")

    def add_member(self, member):
        self.members.append(member)
        print(f"👤 Member '{member.name}' added successfully!")

    # Borrow book
    def borrow_book(self):
        if not self.members or not self.books:
            print("Add members and books first!")
            return

        print("\nAvailable Members:")
        for m in self.members:
            print(f" - {m.name}")
        member_name = input("Enter member name: ").strip()
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print("Member not found!")
            return

        available_books = [b for b in self.books if not b.is_borrowed]
        if not available_books:
            print("No available books to borrow!")
            return

        print("\nAvailable Books:")
        for b in available_books:
            print(f" - {b}")
        book_id = input("Enter book ID: ").strip()
        book = next((b for b in available_books if b.book_id == book_id), None)

        if book:
            book.is_borrowed = True
            due_date = datetime.now() + timedelta(days=7)
            member.borrowed_books.append({"book": book.title, "due_date": due_date.strftime("%Y-%m-%d")})
            self.print_receipt("Borrow", member.name, book.title, due_date)
        else:
            print("Book not available!")

    # Return book
    def return_book(self):
        members_with_books = [m for m in self.members if m.borrowed_books]
        if not members_with_books:
            print("No borrowed books found!")
            return

        print("\nMembers with Borrowed Books:")
        for m in members_with_books:
            print(f" - {m.name}")
        member_name = input("Enter member name: ").strip()
        member = next((m for m in members_with_books if m.name == member_name), None)
        if not member:
            print("Member not found or has no borrowed books!")
            return

        print("\nBorrowed Books by Member:")
        for b in member.borrowed_books:
            print(f" - {b['book']}")
        book_title = input("Enter book title to return: ").strip()
        book = next((bk for bk in self.books if bk.title == book_title and bk.is_borrowed), None)

        if book:
            book.is_borrowed = False
            member.borrowed_books = [b for b in member.borrowed_books if b["book"] != book.title]
            self.print_receipt("Return", member.name, book.title)
        else:
            print("Invalid details or book not borrowed!")

    # Show books and members
    def show_books(self):
        if not self.books:
            print("No books in library yet.")
            return
        print("\n Library Books:")
        for b in self.books:
            print(" -", b)

    def show_members(self):
        if not self.members:
            print("No members in library yet")
            return
        print("\n Library Members:")
        for m in self.members:
            print(" -", m)

    # Digital Receipt (console only)
    def print_receipt(self, action, member_name, book_title, due_date=None):
        print("\n" + "="*50)
        print(f" SMART LIBRARY DIGITAL RECEIPT ({action.upper()})")
        print("-"*50)
        print(f"Member Name : {member_name}")
        print(f"Book Title  : {book_title}")
        print(f"Transaction : {action}")
        print(f"Date & Time : {datetime.now().strftime('%d-%b-%Y %I:%M %p')}")
        if action == "Borrow":
            print(f"Due Date    : {due_date.strftime('%d-%b-%Y')} (7 days)")
        print("-"*50)
        print("Thank you for using Smart Library System")
        print("="*50 + "\n")


def main():
    library = Library()

    while True:
        print("\n========= Library Menu =========")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Books")
        print("6. Show Members")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(Book(title, author))

        elif choice == "2":
            name = input("Enter a member name: ")
            library.add_member(Member(name))

        elif choice == "3":
            library.borrow_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.show_books()

        elif choice == "6":
            library.show_members()

        elif choice == "7":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Try again")


main()


