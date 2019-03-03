from functools import wraps

from flask import session, redirect, url_for

from ..model import Operator, Book


def login_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not is_auth_in():
            return redirect(url_for("page_auth_in"))
        return fn(*args, **kwargs)

    return wrapped


def auth_in(operator: Operator):
    session['uid'] = operator.id


def is_auth_in() -> bool:
    return 'uid' in session


def auth_out():
    session.clear()


def get_operator() -> Operator:
    return Operator.query.get(session['uid'])


def get_operator_id() -> int:
    return session['uid']


def get_book(isbn) -> Book:
    return Book.query.get(isbn)

