import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list
    
    def add_book(self, book_name: str, rating: int):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f"{self.name} has already read {book_name}.")
    
    def has_read(self, book_name: str) -> bool:
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self) -> int:
        return self.num_books
    
    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list['book_rating'] > 3]
