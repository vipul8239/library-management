class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.borrow = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def borrowBook(self, user, book):
        if book not in self.borrow.keys():
            self.borrow.update({book: user})
            print("You can take the book now")
        else:
            print(f"Book is already being used by {self.borrow[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.borrow.pop(book)


if __name__ == '__main__':
    school = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter'], "vipul")

    while True:
        print("Enter your choice to continue")
        print("1. Display Books")
        print("2. Borrow a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            school.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to borrow:")
            user = input("Enter your name")
            school.borrowBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            school.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            school.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
