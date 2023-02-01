class Library:
    books_names = ["Nepali","English","Maths","Science", "Social"]
    
    def __init__(self):
        pass

    def list_of_books(self):
        bnames = '\n'.join(self.books_names)
        print(bnames)

    def get_books(self):
        pass
        

    def return_books(self):
        pass

if __name__ == "__main__":
    l = Library()
    while True:
        try:
            userchoice = input("""Enter
            L - List of books.
            G - Get books.
            R - Return books.""").capitalize()
            if userchoice == 'L':
                l.list_of_books()
            if userchoice == 'G':
                l.get_books()
            if userchoice == 'R':
                l.return_books()
           

        except:
            exit()
