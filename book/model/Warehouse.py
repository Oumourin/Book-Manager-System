from .. import db


class Warehouse(db.Model):
    __tablename__ = 'warehouse'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(256), nullable=False, index=True)
    bookStock = db.relationship('BookStock', backref='warehouse')   # 仓库与图书一对多关系

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Warehouse#{}:{}>'.format(self.id, self.name)
