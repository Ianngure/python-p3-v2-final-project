class Book:
    def __init__(self, id, title, author, available=1):
        self.id = id
        self.title = title
        self.author = author
        self.available = available

class Borrow:
    def __init__(self, id, book_id, borrower, borrow_date, return_date=None):
        self.id = id
        self.book_id = book_id
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.return_date = return_date
