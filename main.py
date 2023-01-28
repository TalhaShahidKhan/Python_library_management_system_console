# Library Management System-
import time


class Library:
    Book = []
    Member = []

    def add_new_book(self, bookname):
        '''Function for adding new books to the library.'''
        self.Book.append(bookname)
        print("A new book added.")

    def display_book(self):
        '''Function for showing the list of books.'''
        print(f"Your Book list is {self.Book}")

    def add_member(self, membername):
        '''Function for adding new member in a library. '''
        self.Member.append(membername)
        print("A new member added.")

    def show_members(self):
        '''Function for showing all the member in the library.'''
        print(f"Your Member list is {self.Member}")

    def cancel_membership(self, membername):
        '''Function for canceling a membership of a member.'''
        self.Member.remove(membername)
        print("Removed Member.")

    def lend_book(self, bookname):
        '''Function for lending book to a member.'''
        if bookname in self.Book:
            print("This book is available!")
            self.Book.remove(bookname)
            print("This book is issued.")
        else:
            print("Sorry, this book is not available!")

    def adding_returned_book(self, bookname):
        '''Function for adding returned book from members'''
        self.Book.append(bookname)


if __name__ == '__main__':
    centralLibrary = Library()
    while True:
        welcomeMsg = """ 
        >>>>>>> Welcome To Central Library <<<<<<
        Please Choice an option =>
            1.Show all books.
            2.Lend a book.
            3.Add a new book.
            4.Add a borrowed book.
            5.Add a member to the library.
            6.Show the member list
            7.Cancel membership.
            8.Exit the Library Management System.
        """
        print(welcomeMsg)
        Weclome_Inp = int(input("Please select an option from above: "))
        if Weclome_Inp == 1:
            centralLibrary.display_book()
        elif Weclome_Inp == 2:
            centralLibrary.display_book()
            req_Book = input("Enter the name of the book from above: ")
            centralLibrary.lend_book(req_Book)
        elif Weclome_Inp == 3:
            addBook = input("Enter the name of the book that you want to add: ")
            centralLibrary.add_new_book(addBook)
        elif Weclome_Inp == 4:
            retbook = input("Enter the name of the returned book: ")
            centralLibrary.adding_returned_book(retbook)
        elif Weclome_Inp == 5:
            memnem = input("Enter the member name: ")
            centralLibrary.add_member(memnem)
        elif Weclome_Inp == 6:
            centralLibrary.show_members()
        elif welcomeMsg == 7:
            canmemnem = input("Enter the name of the member who want to cancel membership: ")
            centralLibrary.cancel_membership(canmemnem)
        elif Weclome_Inp == 8:
            print("Thanks for choosing our app. Have a great day ahead!")
            time.sleep(1)
            exit()
        else:
            print("Please enter a valid input!")
