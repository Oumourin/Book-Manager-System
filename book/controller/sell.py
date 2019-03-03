import datetime
from typing import List

from flask import render_template, request, redirect, url_for, abort

from .. import db, app
from ..handler.session import login_required, get_operator_id, is_auth_in
from ..model import Book, Member, Order, OrderItem, BookStock


@app.route("/sell")
@login_required
def sell_page():
    # 订单默认为空
    sell_order = Order(datetime.datetime.now(), 0, get_operator_id(), 0, 0)
    db.session.add(sell_order)
    db.session.commit()
    order_id = sell_order.id

    return redirect(url_for("sell_page_generated", _id=order_id, login_flag=is_auth_in()))


@app.route("/sell/<int:_id>")
@login_required
def sell_page_generated(_id: int):
    operator_id = get_operator_id()

    sell_order: Order = Order.query.get(_id)
    if sell_order is None:
        return abort(404)

    sell_order_item: List[OrderItem] = sell_order.orderItem
    return render_template(
        "sell.html",
        order_items=sell_order_item,
        order_id=_id,
        operator_id=operator_id,
        login_flag=is_auth_in()
    )


@app.route("/sell/add", methods=['POST'])
@login_required
def sell_order_item_add():
    sell_order_id = get_operator_id()
    isbn = request.form['isbn']
    amount = int(request.form['amount'])

    book = Book.query.get(isbn)
    if book is None:
        return render_template('sell.html', msg="查无此书", login_flag=is_auth_in())

    stock = BookStock.query.filter(BookStock.isbn == isbn).first()
    if stock is None:
        temp_stock = BookStock(isbn, 1, 0)
        db.session.add(temp_stock)
        db.session.commit()
        return render_template('sell.html', msg="无库存记录，已新建该书库存记录", login_flag=is_auth_in())

    if book.bookStock.amount < amount:
        return render_template('sell.html', msg="库存不足！", login_flag=is_auth_in())

    sell_oder_item = OrderItem(sell_order_id, isbn, amount)
    book.bookStock.amount -= amount
    db.session.add(sell_oder_item)
    db.session.commit()
    return redirect(url_for("sell_page_generated", _id=sell_order_id))


@app.route("/sell/remove", methods=['POST'])
@login_required
def sell_order_item_remove():
    item_id = int(request.form['item_id'])
    order_id = int(request.form['order_id'])
    amount = int(request.form['amount'])
    isbn = request.form['isbn']
    book = Book.query.get(isbn)

    item = OrderItem.query.get(item_id)
    if item is None:
        return "查无此项！"

    book.bookStock.amount += amount
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("sell_page_generated", _id=order_id))


@app.route("/sell/submit", methods=['POST'])
def sell_order_item_submit():
    order_id = get_operator_id()
    order: Order = Order.query.get(order_id)
    member_id = request.form['member_id']

    if order is None:
        return "查无此采购清单"

    if member_id is None:
        order.member_id = 0

    order_item: List[OrderItem] = OrderItem.query.filter_by(order_id=order_id).all()

    total_amount: int = 0
    total_price: float = 0.0

    for item in order_item:
        total_amount += item.amount
        total_price += item.amount * item.book.price

    order.total = total_amount
    order.total_price = total_price
    db.session.merge(order)
    db.session.commit()
    return redirect(url_for("page_index"))
