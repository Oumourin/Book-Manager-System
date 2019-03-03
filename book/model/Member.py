from .. import db


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(256), nullable=False, index=True)
    phone = db.Column(db.String(256), nullable=False, index=True)
    email = db.Column(db.String(256), nullable=False, index=True, unique=True)
    level = db.Column(db.Integer, nullable=False)
    delete_flag = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, phone, email, level, delete_flag):
        self.name = name
        self.phone = phone
        self.email = email
        self.level = level
        self.delete_flag = delete_flag

    @property
    def __repr__(self):
        return '<Member#{}:{}:{}:{}:{}>'.format(self.id, self.name, self.phone, self.email, self.level)

