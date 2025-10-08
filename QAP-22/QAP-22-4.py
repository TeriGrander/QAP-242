class LibrarySystem:
    def __init__(self, books) -> None:
        self.books = {}

    def add_book(self, isbn, title, author, year):
        if isbn not in self.books.keys():
            self.books.update({isbn: {'title': title, 'author': author, 'year': year, 'status': 'available'}})
            print(f'Book "{title}" by {author} published in {year} with ISBN {isbn} added to the library')
        else:
            print(f'Book with ISBN {isbn} is already present in the library')

    def change_status(self, isbn, new_status):
        if self.books[isbn]['status'] != new_status:
            self.books[isbn]['status'] = new_status
        else:
            print(f'Book ISBN {isbn} is already {new_status}')

    def search_book(self, isbn):
        if isbn in self.books.keys():
            return f'Book with ISBN {isbn} is "{self.books[isbn]['title']}" by {self.books[isbn]['author']} published in {self.books[isbn]['year']}'
        else:
            return f'No such book in the library'