from . import Book
from . import Order
from .. import db


class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=False)
    isbn = db.Column(db.String(13), db.ForeignKey(Book.isbn), nullable=False)
    amount = db.Column(db.Integer, nullable=False)      # 一个订单中某种书的数目

    def __init__(self, order_id, isbn, amount):
        self.order_id = order_id
        self.isbn = isbn
        self.amount = amount

    def __repr__(self):
        return '<OrderItem#{}:{}:{}:{}>'.format(self.id, self.order_id, self.isbn, self.amount)
