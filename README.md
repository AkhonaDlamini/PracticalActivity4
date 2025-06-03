# 📚 Mini Library Management System in Python

This is a simple Python project designed to simulate basic library management functionalities, including adding books and members to the system. It demonstrates working with lists, dictionaries, functions, and user input.

---

## 📝 Project Overview

The project consists of:

- Creating and displaying lists using both **normal loops** and **list comprehensions**
- Managing a collection of books and members using Python dictionaries inside lists
- Functions to **add books** and **add members**, both with parameters and without parameters (using user input)
- Demonstrating simple data handling without relying on external databases or files

---

## 🔍 Features

- **Book Management**: Add books with attributes like `book_id`, `title`, `author`, and `status`
- **Member Management**: Add members with `member_id`, `name`, and a list of `borrowed_books`
- Use of **normal loops** and **list comprehensions** to process and display data
- Functions that accept input from the user to dynamically add books or members without predefined parameters

---

## 💡 What You Will Learn

- How to work with lists and dictionaries in Python to model real-world entities
- The difference between using normal loops and list comprehensions for list creation
- Defining functions with and without parameters
- Taking user input to dynamically modify data structures
- Basic data organization for a mini library system

---

## ⚙️ How to Use

1. Run the script containing the functions `add_book()` and `add_member()` to add books and members interactively.
2. Observe how books and members are stored as dictionaries inside lists.
3. Modify or extend the lists to simulate borrowing, returning, or other library functions (future improvements).

---

## 🛠️ Example Code Snippets

```python
# Normal list creation
codes = [14, 15, 16, 17, 18, 19, 20]
new_c = []
for code in codes:
   new_c.append(code)
print("Normal list:", new_c)

# List comprehension
new_codes = [code for code in codes]
print("Comprehensive list:", new_codes)

# Adding a book with parameters
def add_book(book_id, title, author, status):
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })
    return books

# Adding a member without parameters (interactive)
def add_member():
    members = []
    member_id = int(input("Enter member id: "))
    name = input("Enter your name: ")
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
    })
    return members
