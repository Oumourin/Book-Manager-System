# 弃坑！！！
# from book.handler.session import login_required, get_book
# from book.model import BookStock, SupplierBook,PurchaseOrderItem
# from book import db, app
#
# from flask import request, redirect, url_for, render_template, flash
#
#
# @app.route('/manager/book/delete', methods=['GET', 'POST'])
# @login_required
# def delete_book_page():
#     if request.method == 'GET':
#         return render_template('delete_book.html')
#
#     isbn = request.form['isbn']
#     book = get_book(isbn)
#
#     if book is None:
#         return "书籍不存在！"
#
#     get_stock = BookStock.query.filter(BookStock.isbn == isbn).all()
#     get_supplier = SupplierBook.query.filter(SupplierBook.isbn == isbn).all()
#     get_purchase_order_item = PurchaseOrderItem.query.filter(PurchaseOrderItem.isbn == isbn).all()
#     if get_purchase_order_item is not None:
#         for item in get_purchase_order_item:
#             db.session.delete(item)
#             db.session.commit()
#
#     if get_supplier is not None:
#         for item in get_supplier:
#             db.session.delete(item)
#             db.session.commit()
#
#     if get_stock is not None:
#         for item in get_stock:
#             db.session.delete(item)
#             db.session.commit()
#
#     db.session.delete(book)
#     db.session.commit()
#     flash("删除完毕！")
#     return redirect(url_for('delete_book_page'))
#
#
# @app.route('/manager/delete/submit', methods=['POST'])
# @login_required
# def delete_submit_page():
#     return redirect(url_for('page_index'))
