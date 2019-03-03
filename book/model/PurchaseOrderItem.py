from . import Book
from .. import db


class PurchaseOrderItem(db.Model):
    __tablename__ = 'purchase_order_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey("purchase_order.id"), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.id"), nullable=False)
    isbn = db.Column(db.String(13), db.ForeignKey(Book.isbn), nullable=False)
    amount = db.Column(db.Integer, nullable=False)      # 买入的某种书的数量

    def __init__(self, purchase_order_id, supplier_id, isbn, amount):
        self.purchase_order_id = purchase_order_id
        self.supplier_id = supplier_id
        self.isbn = isbn
        self.amount = amount

    def __repr__(self):
        return '<PurchaseOrderItem#{}:{}:{}:{}:{}>'.format(self.id, self.purchase_order_id, self.supplier_id, self.isbn,
                                                           self.amount)
