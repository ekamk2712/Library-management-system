from add import add_book 
from show import show_books 
from borrow import borrow_book 
from return_book import return_book 
def library():
    while True:
        print("Menue")
        print("1.Add book")
        print("2.Show books")
        print("3.Borrow book")
        print("4.Return book")
        print("5.Exit")
        choice=int(input("Enter the choice:"))
        if choice==1:
            add_book()
        elif choice==2:
            show_books()
        elif choice==3:
            borrow_book()
        elif choice==4:
            return_book()
        elif choice==5:
            print("Thank you! Visit again")
            break
        else:
            print("Invalid choice")
library()