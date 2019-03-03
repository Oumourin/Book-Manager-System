from . import Operator
from .. import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    time = db.Column(db.DateTime, nullable=False, index=True)
    member_id = db.Column(db.Integer, nullable=True)
    operator_id = db.Column(db.Integer, db.ForeignKey(Operator.id), nullable=False)
    total = db.Column(db.Float, nullable=False)     # 卖出书的数目
    total_price = db.Column(db.Float, nullable=False)       # 卖出书的总价
    orderItem = db.relationship('OrderItem', backref='order')  # 订单和订单单项一对多关系

    def __init__(self, time, member_id, operator_id, total, total_price):
        self.time = time
        self.member_id = member_id
        self.operator_id = operator_id
        self.total = total
        self.total_price = total_price

    def __repr__(self):
        return '<Order#{}:{}:{}:{}:{}:{}>'.format(self.id, self.time, self.member_id, self.operator_id, self.total,
                                                  self.total_price)

