class Library:
    books_names = {"Nepali","English","Maths","Science", "Social"}
    total_book_names = ["Nepali","English","Maths","Science", "Social"]
    
    def __init__(self):
        pass
    
    def list_of_books(self):
        bnames = '\n'.join(self.books_names)
        print(bnames)

    def get_books(self):
        self.list_of_books()
        print("\n")
        userchoice = input("Enter the name of book you want:\n").title()
        if userchoice in self.books_names:
            print ("Take the book")
            self.books_names.discard(userchoice)
            print(self.books_names)
        else:
            print("Sorry!!Book is not available.")
        

    def return_books(self):
        userchoice = input("Enter the name of the book you want to return").title()
        if userchoice in self.total_book_names :
            self.books_names.add(self.userchoice)
            print(self.books_names)
        else :
            print("The name of book was invalid")
            


if __name__ == "__main__":
    l = Library()
    while True:
        try:
            userchoice = input("""Enter
            L - List of books.
            G - Get books.
            R - Return books.:-\n""").capitalize()
            if userchoice == 'L':
                l.list_of_books()
            if userchoice == 'G':
                l.get_books()
            if userchoice == 'R':
                l.return_books()
           

        except:
            ValueError()
        
        finally:
            userchoice = input("""Enter S - stay 
Any other key - Exit""").capitalize()
            if userchoice == 'S':
                continue
            else:
                exit()
