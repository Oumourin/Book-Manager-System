from flask import render_template

from ..handler.session import is_auth_in
from .. import app


@app.route("/")
def page_index():
    return render_template("index.html", login_flag=is_auth_in())
    # return render_template("base.html")


# @app.route("/test")
# def test_page():
#     return render_template("")
