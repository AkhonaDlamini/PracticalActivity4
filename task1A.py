books = []
members = []

def add_book(book_id,title,author,status):

    books.append({
        "book_id":book_id,
        "title":title,
        "author":author,
        "status":status
    })

    return books


def add_member(member_id,name):

    members.append({
        "member_id":member_id,
        "name":name,    
        "borrowed_books":[]
    })

    return members


add_book(2024001,"Python Programming","Jacob Zuma","Pending")
add_member(1,"Anelisa Maleka")
print(books)
print(members)