from book import db
# noinspection PyUnresolvedReferences
from book.model import *

db.create_all()
default = Operator('test', 'test@test.com', 'test123')
default.set_password()
db.session.add(default)
db.session.commit()

if __name__ == '__main__':
    from book import app
    # noinspection PyPackageRequirements
    from gevent.pywsgi import WSGIServer

    WSGIServer(('0.0.0.0', 8080), app).serve_forever()
