from .. import db


class SupplierBook(db.Model):
    __tablename__ = 'supplier_book'
    isbn = db.Column(db.String(13), db.ForeignKey("book.isbn"), nullable=False, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.id"), nullable=False, primary_key=True)

    def __init__(self, isbn, supplier_id):
        self.isbn = isbn
        self.supplier_id = supplier_id

    def __repr__(self):
        return '<SupplierBook#{}:{}>'.format(self.isbn, self.supplier_id)
