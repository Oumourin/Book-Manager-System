from .. import db


class BookStock(db.Model):
    __tablename__ = 'book_stock'
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn'), nullable=False, primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), nullable=False, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    book = db.relationship('Book', uselist=False)   # 书和书库存一对一关系

    def __init__(self, isbn, warehouse_id, amount):
        self.isbn = isbn
        self.warehouse_id = warehouse_id
        self.amount = amount

    def __repr__(self):
        return '<BoolStock#{}:{}:{}>'.format(self.isbn, self.warehouse_id, self.amount)
