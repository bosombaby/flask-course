from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Flask"


if __name__ == "__main__":
    # 自动刷新
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host="0.0.0.0")
