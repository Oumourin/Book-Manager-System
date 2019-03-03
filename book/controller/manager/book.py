from book import app, db
from book.model import Book, Supplier, Warehouse, BookStock, SupplierBook
from book.handler.session import login_required, is_auth_in

from flask import request, redirect, flash, url_for, render_template


@app.route('/manager/book/add', methods=['GET', 'POST'])
@login_required
def add_book_page():
    if request.method == 'GET':
        return render_template("addbook.html", login_flag=is_auth_in())

    book_name = request.form['name']
    book_isbn = request.form['isbn']
    book_price = request.form['price']
    book_author = request.form['author']
    book_press = request.form['press']
    book_purchase_price = request.form['purchase_price']
    # book_supplier = request.form['id']
    # book_warehouse = request.form['warehouse']
    # book_amount = request.form['amount']
    check_book = Book.query.get(book_isbn)
    # check_supplier = Supplier.query.get(book_supplier)
    # check_warehouse = Warehouse.query.get(book_warehouse)

    if check_book is not None:
        return render_template('addbook.html', msg='书籍已存在！')

    # if check_supplier is None:
    #     return render_template('addbook.html', msg="供应商不存在！")
    #
    # if check_warehouse is None:
    #     return render_template('addbook.html', msg="无此仓库")

    # if book_amount is None:
    #     book_amount = 0

    book = Book(book_isbn, book_name, book_price, book_author,
                book_press, book_purchase_price, True)
    db.session.add(book)
    db.session.commit()
    # book_stock = BookStock(book_isbn, id, book_amount)
    # db.session.add(book_stock)
    # # supplier = SupplierBook(book_isbn, book_supplier)
    # # db.session.add(supplier)
    # db.session.commit()
    flash('添加成功！')
    return redirect(url_for('add_book_page'))


@app.route('/manager/book/submit', methods=['POST'])
@login_required
def submit_add_page():
    return redirect(url_for('page_index'))


@app.route('/manager/book/delete', methods=['GET', 'POST'])
@login_required
def delete_book_page():
    if request.method == 'GET':
        return render_template('delete_book.html', login_flag=is_auth_in())

    isbn = request.form['isbn']
    book = Book.query.get(isbn)
    book.delete_flag = 0
    db.session.commit()
    flash("删除成功")
    return render_template('delete_book.html', login_flag=is_auth_in())



