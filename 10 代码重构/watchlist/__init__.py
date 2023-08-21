from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path, "data.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "需要登录"


@login_manager.user_loader
def load_user(user_id):
    from .models import User

    user = User.query.get(int(user_id))
    return user


# 全局模板上下文处理
@app.context_processor
def inject_user():
    from .models import User

    user = User.query.first()
    return dict(user=user)


from . import views, errors, models
