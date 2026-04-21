from data import books 
def show_books():
    if len(books)==0:
        print("No books avaliable")
    else:
        print("Avaliable books")
        for book in books:
            print(book)