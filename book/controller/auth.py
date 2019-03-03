from flask import render_template, request, redirect, url_for

from .. import app
from ..handler.session import auth_in, auth_out, login_required, is_auth_in
from ..model import Operator


@app.route("/auth/in", methods=['POST', 'GET'])
def page_auth_in():
    if request.method == 'GET':
        return render_template("auth_in.html", login_flag=is_auth_in())

    username = request.form['username']
    password = request.form['password']

    operator = Operator.query.filter(Operator.mail == username).first()
    if operator is None:
        return render_template("auth_in.html", msg='邮箱不存在，请重新输入！')

    if not operator.check_password(password):
        return render_template("auth_in.html", msg='密码错误，请核对密码检查大小写再次尝试！')

    auth_in(operator)
    return redirect("/")


@app.route("/auth/out", methods=['GET'])
@login_required
def page_auth_out():
    auth_out()
    return redirect(url_for("page_index"))
