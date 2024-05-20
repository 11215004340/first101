# Initialize empty lists, sets, and dicttionary
books_list = []
authors_set = set()
books_dict = {}

# Add books 
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Structure and Algorithms")
authors_set.add("Jane Doe")
books_dict["data Structure and Algorithms"] = "Jane Doe"
 
books_list.append("Machine Learning basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning basics"] = "Alice Johnson"
# Search for a book 
search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Books found! Author: {books_dict[search_title]}")
else:
    print("Book not found!")
# Display all books
print("Lists of books:")
for books in books_list:
     print(books)
# Remove a book
remove_title = input("Enter the title of the book to remove or else enter the skips: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
    print("Books available: ", books_list)

else:
    print("Book not found!")