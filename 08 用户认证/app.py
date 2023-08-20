from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path, "data.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)


# 创建数据库模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


def create_data():
    # 第一次使用
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
    print("添加完成")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year) < 4 or len(title) > 60:
            flash("创建失败!")
            return redirect(url_for("index"))
        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash("创建成功!")
        return redirect(url_for("index"))
    else:
        movies = Movie.query.all()
        return render_template("index.html", movies=movies)


# 编辑条目
@app.route("/movie/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year) < 4 or len(title) > 60:
            flash("更新失败!")
            return redirect(url_for("edit", movie_id=movie_id))

        movie.title = title
        movie.year = year
        db.session.commit()
        flash("更新成功!")
        return redirect(url_for("index"))

    return render_template("edit.html", movie=movie)


# 删除条目
@app.route("/movie/delete/<int:movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("删除成功!")
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
