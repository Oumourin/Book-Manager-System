from book.model import warehouse, Book
from book.handler.session import login_required, is_auth_in

from flask import request, render_template

from book import db, app


@app.route('/manager/warehouse')
@login_required
def warehouse_page():
    return render_template('warehouse_manager.html', login_flag=is_auth_in())


@app.route('/manager/warehouse/add')
@login_required
def warehouse_add_page():
    return


@app.route('/manager/warehouse/delete')
@login_required
def warehouse_delete_page():
    return


@app.route('/manager/warehouse/delete')
@login_required
def warehouse_modify_page():
    return
