from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import click
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)


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


# 创建数据库模型
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


@app.cli.command()
def init():
    # 第一次使用
    db.drop_all()
    db.create_all()
    name = "bosom"
    movies = [
        {"title": "My Neighbor Totoro", "year": "1988"},
        {"title": "Dead Poets Society", "year": "1989"},
        {"title": "A Perfect World", "year": "1993"},
        {"title": "Leon", "year": "1994"},
        {"title": "Mahjong", "year": "1996"},
        {"title": "Swallowtail Butterfly", "year": "1996"},
        {"title": "King of Comedy", "year": "1999"},
        {"title": "Devils on the Doorstep", "year": "1999"},
        {"title": "WALL-E", "year": "2008"},
        {"title": "The Pork of Music", "year": "2012"},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m["title"], year=m["year"])
        db.session.add(movie)

    db.session.commit()
    click.echo("添加完成")


# 生成管理员账户
@app.cli.command()
@click.option("--username", prompt=True, help="The username used to login.")
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="The password used to login.",
)
def admin(username, password):
    user = User.query.first()

    if user is not None:
        click.echo("更新管理员")
        user.username = username
        user.set_password(password)
    else:
        click.echo("创建管理员")
        user = User(username=username, name="Admin")
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo("完成创建")


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.first()
        if not username or not password or len(password) < 6:
            flash("格式错误")
        elif user.username == username and user.validate_password(password):
            login_user(user)
            flash("登录成功")
            return redirect(url_for("index"))
        else:
            flash("账号或密码错误")

    return render_template("login.html")


# 账号登出
@app.route("/logout")
def logout():
    logout_user()
    flash("退出账号")
    return redirect(url_for("index"))


# 修改用户的名字
@app.route("/setting", methods=["GET", "POST"])
@login_required
def setting():
    if request.method == "POST":
        name = request.form.get("name")
        if not name or len(name) < 3 or len(name) > 20:
            flash("名称不符合规范")
            return redirect(url_for("setting"))
        else:
            current_user.name = name
            db.session.commit()
            flash("更新成功")
            return redirect(url_for("index"))
    return render_template("setting.html")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not current_user.is_authenticated:  # 如果当前用户未认证
            flash("请登录")
            return redirect(url_for("index"))  # 重定向到主页
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year) < 4 or len(title) > 60:
            flash("创建失败")
            return redirect(url_for("index"))
        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash("创建成功")
        return redirect(url_for("index"))
    else:
        movies = Movie.query.all()
        return render_template("index.html", movies=movies)


# 编辑条目
@app.route("/movie/edit/<int:movie_id>", methods=["GET", "POST"])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year) < 4 or len(title) > 60:
            flash("更新失败")
            return redirect(url_for("edit", movie_id=movie_id))

        movie.title = title
        movie.year = year
        db.session.commit()
        flash("更新成功")
        return redirect(url_for("index"))

    return render_template("edit.html", movie=movie)


# 删除条目
@app.route("/movie/delete/<int:movie_id>", methods=["GET", "POST"])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for("index"))


# 全局模板上下文处理
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    # 自动刷新
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host="0.0.0.0")
