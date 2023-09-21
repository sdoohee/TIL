class Book:
    nation = "Korea" # 클래스 변수

    def __init__(self, book_no, book_name, author, price, stock, publisher):
        self.book_no = book_no
        self.book_name = book_name
        self.author = author
        self.price = price
        self.stock = stock
        self.publisher = publisher

    def get_book_no(self):
        return self.book_no

    def get_book_name(self):
        return self.book_name

    def get_book_author(self):
        return self.author