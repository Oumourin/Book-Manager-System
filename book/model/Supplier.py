from .. import db


class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = db.Column(db.String(256), nullable=False, unique=True, index=True)
    supplierBook = db.relationship('SupplierBook', backref='supplier')      # 供应商和供应的书籍一对多关系
    purchaseOrderItem = db.relationship('PurchaseOrderItem', backref='supplier')    # 供应商和采购流水一对多关系

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Supplier#{}:{}>'.format(self.id, self.name)
