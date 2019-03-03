import datetime
from typing import List

from flask import render_template, request, redirect, url_for, abort, flash

from .. import db, app
from ..handler.session import login_required, get_operator_id, is_auth_in
from ..model import PurchaseOrder, PurchaseOrderItem, Book


@app.route("/purchase")
@login_required
def purchase_page():
    order = PurchaseOrder(datetime.datetime.now(), get_operator_id(), 0, 0)
    db.session.add(order)
    db.session.commit()

    return redirect(url_for("purchase_page_generated", _id=order.id))


@app.route("/purchase/<int:_id>")
@login_required
def purchase_page_generated(_id: int):
    operator_id = get_operator_id()

    order: PurchaseOrder = PurchaseOrder.query.get(_id)
    if order is None:
        return abort(404)

    order_items: List[PurchaseOrderItem] = order.purchaseOrderItem
    return render_template(
        "purchase.html",
        operator_id=operator_id,
        order_id=_id,
        order_items=order_items,
        login_flag=is_auth_in()
    )


@app.route("/purchase/add", methods=['POST'])
@login_required
def order_purchase_item_add():
    order_id = request.form['order_id']
    isbn = request.form['isbn']
    amount = int(request.form['amount'])

    book = Book.query.get(isbn)
    if book is None:
        return render_template('purchase.html', login_flag=is_auth_in(), msg='书籍不存在！')

    if len(book.supplier) == 0:
        return render_template('purchase.html', login_flag=is_auth_in(), msg='无可用供货商')

    if not book.delete_flag:
        return render_template('purchase.html', login_flag=is_auth_in(), msg='书籍不存在！')

    order_item = PurchaseOrderItem(order_id, book.supplier[0].supplier_id, isbn, amount)
    book.bookStock.amount += amount     # 更新库存
    db.session.add(order_item)
    db.session.commit()
    return redirect(url_for("purchase_page_generated", _id=order_id))


@app.route("/purchase/remove", methods=['POST'])
@login_required
def order_purchase_item_remove():
    item_id = int(request.form['item_id'])
    order_id = int(request.form['order_id'])
    amount = int(request.form["amount"])
    isbn = request.form["isbn"]
    book = Book.query.get(isbn)

    item = PurchaseOrderItem.query.get(item_id)
    if item is None:
        return "查无此项！"

    book.bookStock.amount -= amount
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("purchase_page_generated", id=order_id))


@app.route("/purchase/submit", methods=['POST'])
def order_purchase_submit():
    order_id = int(request.form['order_id'])
    order: PurchaseOrder = PurchaseOrder.query.get(order_id)

    if order is None:
        return "查无此采购清单"

    order_items: List[PurchaseOrderItem] = PurchaseOrderItem.query.filter_by(purchase_order_id=order_id).all()

    total_amount: int = 0
    total_price: float = 0.0

    for item in order_items:
        total_amount += item.amount
        total_price += item.amount * item.book.purchase_price

    order.total = total_amount
    order.total_price = total_price
    db.session.merge(order)
    db.session.commit()
    flash("提交成功")
    return redirect(url_for("page_index"))

#
# @app.route('/add_warehouse', methods=["GET", "POST"])
# @login_required
# def add_warehouse_page():
#     get_operator = request.form['operator']
#     check_operator = Operator.query.filter(Operator.id == get_operator).first()
#     if check_operator is None:
#         return render_template("purchase.html", msg="操作员不存在")
#
#     create_purchase_order = PurchaseOrder(datetime.datetime.now(), get_operator, 0, 0)      # 初始化采购单
#     db.session.add(create_purchase_order)
#     db.session.commit()     # 提交采购单
#     purchase_id = create_purchase_order.id      # 获取表单ID
#     temp = 1
#     while request.form["book"+str(temp)] != "null":
#         book_name = request.form["book"+str(temp)]
#         book_amount = request.form["amount"+str(temp)]
#         # 查询相关信息
#         get_book = Book.query.filter(Book.name == book_name).first()
#         get_book_isbn = get_book.isbn
#         get_book_stock = BookStock.query.filter(BookStock.isbn == get_book_isbn).first()
#         get_supplier = SupplierBook.query.filter(SupplierBook.isbn == get_book_isbn).first()  # ???????
#         get_supplier_id = get_supplier.supplier_id
#         # 建立采购流水
#         create_purchase_order_item = PurchaseOrderItem(purchase_id, get_supplier_id, get_book_isbn, int(book_amount))
#         # 更新采购单信息
#         create_purchase_order.total += int(book_amount)
#         get_book_stock.amount += int(book_amount)
#         get_book_total_price = get_book.purchase_price * float(book_amount)
#         create_purchase_order.total_price += float(get_book_total_price)
#         # 提交流水
#         db.session.add(create_purchase_order_item)
#         db.session.commit()
#
#     return render_template("addstock.html", get_total_amount=create_purchase_order.total,
#                            get_total_price=create_purchase_order.total_price)
#
# #so repeat me the problem
# # 设置断点的话会在get_book那里报错
# #第二次循环
# # 1.使用书名当订单项目比较傻逼
# # 毕竟 ISBN 可以用扫码枪直接输入，书名还得打汉字
#
# # 2 程序逻辑设计有点问题
# #  如果这样呢 直接爆炸（
# # 这样吧 我给你改写一个
