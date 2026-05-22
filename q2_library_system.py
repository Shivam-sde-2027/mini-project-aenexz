def add_book(catalog,book_id,title,author,year):
    catalog[book_id]={title,author,year}
    print(f"Book '{title}' added successfully")


def borrow_book(catalog,borrowed_books,book_id):
    if book_id not in catalog:
        print("Book does not exist.")
    elif book_id in borrowed_books:
        print("Book is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Book ID {book_id} borrowed successfully.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print("Book was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)   


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


def main():
    catalog={}
    borrowed_books=[]
    members=set()

    add_book(catalog,101,"Python Basics","John Smith",2020)
    add_book(catalog,102,"Data Structures","Alice Brown",2019)
    add_book(catalog,103,"Machine Learning","David Lee",2021)
    add_book(catalog,104,"Cyber Security","Emma Wilson",2022)

    register_member(members,1)
    register_member(members,2)
    register_member(members,3)
    register_member(members,2)

    print("\nRegistered Members:", members)

    borrow_book(catalog,borrowed_books,101)
    borrow_book(catalog,borrowed_books,103)

    return_book(borrowed_books, 101)

    show_available(catalog, borrowed_books)
main()

