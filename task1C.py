#Rewrite the entire task 1B without using functions

books = []
book_id = int(input("Enter the book id of the book you want to add:"))
title = input("Enter the title of the book you want to add:")
author = input("Enter the author of the book you want to add:")
status = input("Enter the status of the book (pending/borrowed,/in shelf):")

books.append({
    "book_id":book_id,
    "title":title,
    "author":author,
    "status":status
})

print(books)

members = []
member_id = int(input("Enter member id:"))
name =input("Enter your name:")
    
members.append({
    "member_id":member_id,
    "name": name,
    "borrowed_books": []
})

print(members)