from .. import db


class Book(db.Model):
    __tablename__ = 'book'
    isbn = db.Column(db.String(13), primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False, index=True)
    price = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(256), nullable=False, index=True)
    press = db.Column(db.String(256), nullable=False, index=True)
    purchase_price = db.Column(db.Float, nullable=False)
    delete_flag = db.Column(db.Boolean, nullable=False)                  # 删除标志位
    bookStock = db.relationship('BookStock', uselist=False)        # 书和库存信息一对一关系
    supplier = db.relationship('SupplierBook', backref='book')      # 书和供应商一对多关系
    orderItem = db.relationship('OrderItem', backref='book')        # 书和订单单项一对多关系
    purchaseOrderItem = db.relationship('PurchaseOrderItem', backref='book')    # 书和采购流水一对多关系

    def __init__(self, isbn, name, price, author, press, purchase_price, delete_flag):
        self.isbn = isbn
        self.name = name
        self.price = price
        self.author = author
        self.press = press
        self.purchase_price = purchase_price
        self.delete_flag = delete_flag

    def __repr__(self):
        return '<Book#{}:{}:{}:{}:{}>'.format(self.isbn, self.name, self.price, self.author, self.press)






