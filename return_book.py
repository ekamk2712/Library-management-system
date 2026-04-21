from data import books,issued_books 
def return_book():
    name=input("Enter the book name you want to return?")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name,'is returned')
    else:
        print(name,'The book was not issued')