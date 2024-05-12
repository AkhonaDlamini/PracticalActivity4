import pandas as pd

book_id = int(input("Enter book id:"))
title = input("Enter the title of the book:")
author = input("Enter the author of the book:")
status = input("Enter book status (Pending/Borrowed/In shelf):")

books = {'book_id':book_id,'title':title,'author':author,'status':status}
data = pd.DataFrame(books, index=[1])
print(data)

member_id = int(input("Enter member id:"))
name = input("Enter your name:")

members = {'member_id':member_id,'name':name,'borrowed_books':[2]}
df = pd.DataFrame(members,index = [1])
print(df)