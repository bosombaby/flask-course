from . import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import User, Movie
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
)


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
