from book import app
from ..model import Book, BookStock

from flask import request, render_template

from ..handler.session import login_required, is_auth_in


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search_page():
    if request.method == 'GET':
       return render_template('search.html', login_flag=is_auth_in())

    search = request.form['search']
    search_name = Book.query.filter(Book.name.like('%'+search+'%')).all()
    search_isbn = Book.query.filter(Book.isbn.ilike("%"+search+"%")).all()

    return render_template('search_result.html', login_flag=is_auth_in(),
                           order_items_isbn=search_isbn, order_items_name=search_name, msg=search)


@app.route('/manager', methods=['POST'])
def return_index():
    return render_template('index.html', login_flag=is_auth_in())
