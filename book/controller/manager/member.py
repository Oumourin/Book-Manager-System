from book.model import Member
from book.handler.session import login_required, is_auth_in

from flask import request, render_template, url_for, redirect, flash

from book import db, app


@app.route('/manager/member')
@login_required
def member_manager():
    return render_template("membermanager.html", login_flag=is_auth_in())


@app.route('/manager/member/modify/', methods=['POST', 'GET'])
@login_required
def member_modify_page():
    if request.method == 'GET':
        return render_template('modify_member.html', login_flag=is_auth_in())
    new_name = request.form['name']
    new_phone = request.form['phone']
    email = request.form['email']
    new_level = request.form['level']
    new_email = request.form['new_email']
    member = Member.query.filter(Member.email == email).first()

    if member is None:
        return render_template('membermanager.html', msg="用户不存在")

    if new_name != "":
        member.name = new_name

    if new_phone != "":
        member.phone = new_phone

    if new_email != "":
        member.email = new_email

    if new_level != "":
        member.level = new_level

    db.session.commit()
    flash('修改完成！')
    return redirect(url_for('member_manager'))


@app.route('/manager/member/add', methods=['GET', 'POST'])
@login_required
def add_member_page():
    if request.method == 'GET':
        return render_template('add_member.html', login_flag=is_auth_in())

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    level = request.form['level']
    check_member = Member.query.filter(Member.email == email).first()

    if check_member is not None:
        return render_template('membermanager.html', login_flag=is_auth_in(), msg='会员已存在！')

    member = Member(name, phone, email, level, True)
    db.session.add(member)
    db.session.commit()
    flash("添加成功！")
    return redirect(url_for("member_manager"))


@app.route('/manager/member/submit')
@login_required
def submit_member_page():
    redirect(url_for('member_manager'))


@app.route('/manager/member/delete', methods=['GET', 'POST'])
@login_required
def delete_member_page():
    if request.method == 'GET':
        return render_template('delete_member.html', login_flag=is_auth_in())

    email = request.form['email']

    if email is None:
        return render_template('membermanager.html', login_flag=is_auth_in(), msg="邮箱不存在")

    member = Member.query.filter(Member.email == email).first()

    if member is None:
        return render_template('membermanager.html', login_flag=is_auth_in(), msg="用户不存在")

    if member.delete_flag == False:
        return render_template('membermanager.html', login_flag=is_auth_in(), msg='用户已删除！')
    member.delete_flag = False
    db.session.commit()
    flash('删除成功！')
    return redirect(url_for('member_manager'))
