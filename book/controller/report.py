from ..model import PurchaseOrder, Order
from book import app
from flask import render_template
from ..handler.session import login_required


@app.route('/report')
@login_required
def report_page():
    order_amount = Order.query.count()      # 获取订单条数
    # operator_id = request.form["operator"]      # 获取操作员Id
    # order_item_amount = OrderItem.query.count()      # 获取订单流水数量
    purchase_amount = PurchaseOrder.query.count()   # 获取采购单条数
    order_total = 0
    purchase_total = 0
    finance_total = 0.0
    cost_total = 0.0

    if purchase_amount == 0:        # 数据为零处理
        purchase_total = 0
        cost_total = 0.0

    else:
        for i in range(1, purchase_amount+1):
            temp_purchase = PurchaseOrder.query.filter(PurchaseOrder.id == i).first()
            purchase_total += temp_purchase.total
            cost_total += temp_purchase.total_price

    if order_amount == 0:        # 数据为零处理
        order_total = 0
        finance_total = 0
    else:
        for i in range(1, order_amount+1):
            temp_order = Order.query.filter(Order.id == i).first()
            order_total += temp_order.total
            finance_total += temp_order.total_price

    profit_total = finance_total - cost_total

    # if order_item_amout == 0:        # 数据为零处理
    #     finance_total = 0
    # else:
    #     for i in range(1, order_item_amount+1):
    #         get_order_item = OrderItem.query.filter(OrderItem.id == i).first()
    #         get_book_isbn = get_order_item.isbn
    #         get_book = Book.query.filter(Book.isbn == get_book_isbn).first()
    #         get_price = get_book.price
    #         get_total_price = get_price*get_order_item.amount
    #         finance_total += get_total_price

    return render_template("replenishment.html", purchase_total=purchase_total, order_total=order_total,
                           finance_total=finance_total, profit_total=profit_total)


