from .. import db
from werkzeug.security import generate_password_hash, check_password_hash


class Operator(db.Model):
    __tablename__ = 'operator'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(256), nullable=False, unique=True, index=True)
    mail = db.Column(db.String(256), nullable=False, index=True, unique=True)
    password = db.Column(db.String(256), nullable=False)
    order = db.relationship('Order', backref='operator')        # 操作员和订单一对多关系
    purchaseOrder = db.relationship('PurchaseOrder', backref='operator')   # 操作员和采购单一对多关系

    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    def set_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<Operator#{}:{}:{}:{}>'.format(self.id, self.name, self.mail, self.password)

