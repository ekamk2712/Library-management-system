from data import books 
def add_book():
    name=input("Enter the name of the book:")
    books.append(name)
    print(name,'is added')