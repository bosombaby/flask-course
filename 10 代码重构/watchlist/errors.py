from flask import render_template
from . import app


# 错误处理函数
@app.errorhandler(400)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template("errors/400.html"), 400


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template("errors/500.html"), 500
