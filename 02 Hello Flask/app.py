from flask import Flask, url_for
from markupsafe import escape


app = Flask(__name__)


# 一个视图函数也可以绑定多个 URL
@app.route("/")
@app.route("/index")
@app.route("/home")
def view_text():
    return "Hello Flask!"


@app.route("/png")
def view_png():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# 获取路径参数
@app.route("/user/<name>")
def view_user(name):
    return f"<h1>User:{name}</h1>"


# 测试url_for
@app.route("/test/url_for")
def test_url_for():
    print(url_for("view_text"))
    print(url_for("view_png"))
    print(url_for("view_user", name="test_url_for"))
    print(url_for("test_url_for", name="bosom"))
    return "test_url_for"


if __name__ == "__main__":
    app.run()
