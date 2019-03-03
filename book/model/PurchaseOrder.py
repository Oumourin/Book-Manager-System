from . import Operator
from .. import db


class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    time = db.Column(db.DateTime, nullable=False, index=True)
    operator_id = db.Column(db.Integer, db.ForeignKey(Operator.id), nullable=False)
    total = db.Column(db.Integer, nullable=False)       # 买入书的总数
    total_price = db.Column(db.Float, nullable=False)     # 购书总金额
    purchaseOrderItem = db.relationship('PurchaseOrderItem', backref='purchaseOrder')   # 采购单和采购单流水一对多关系

    def __init__(self, time, operator_id, total, total_price):
        self.time = time
        self.operator_id = operator_id
        self.total = total
        self.total_price = total_price

    def __repr__(self):
        return '<PurchaseOrder#{}:{}:{}:{}:{}>'.format(self.id, self.time, self.operator_id, self.total,
                                                       self.total_price)
