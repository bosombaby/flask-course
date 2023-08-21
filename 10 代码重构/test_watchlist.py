import unittest
from watchlist import app, db
from watchlist.models import User, Movie
from watchlist.commands import init, admin


class WatchlistTestCase(unittest.TestCase):
    def setUp(self):
        # 更新配置
        app.config.update(TESTING=True, SQLALCHEMY_DATABASE_URI="sqlite:///:memory:")
        # 创建数据库和表
        db.create_all()
        # 创建测试数据，一个用户，一个电影条目
        user = User(name="Test", username="bosom")
        user.set_password("123456")
        movie = Movie(title="Test Movie Title", year="2019")
        # 使用 add_all() 方法一次添加多个模型类实例，传入列表
        db.session.add_all([user, movie])
        db.session.commit()

        self.client = app.test_client()  # 创建测试客户端
        self.runner = app.test_cli_runner()  # 创建测试命令运行器

    def tearDown(self):
        db.session.remove()  # 清除数据库会话
        db.drop_all()  # 删除数据库表

    # 测试程序实例是否存在
    def test_app_exist(self):
        self.assertIsNotNone(app)

    # 测试程序是否处于测试模式
    def test_app_is_testing(self):
        self.assertTrue(app.config["TESTING"])

    # 测试 404 页面
    def test_404_page(self):
        response = self.client.get("/nothing")  # 传入目标 URL
        data = response.get_data(as_text=True)
        self.assertIn("Page Not Found - 404", data)
        self.assertIn("Go Back", data)
        self.assertEqual(response.status_code, 404)  # 判断响应状态码

    # 测试主页
    def test_index_page(self):
        response = self.client.get("/")
        data = response.get_data(as_text=True)
        self.assertIn("Titles", data)
        self.assertEqual(response.status_code, 200)

    # 辅助方法，用于登入用户
    def login(self):
        response = self.client.post(
            "/login",
            data=dict(username="bosom", password="123456"),
            follow_redirects=True,
        )
        data = response.get_data(as_text=True)

    # 测试创建条目
    def test_create_item(self):
        self.login()
        # 测试创建条目操作（成功）
        response = self.client.post(
            "/", data=dict(title="New Movie1", year="2019"), follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn("创建成功", data)
        self.assertIn("New Movie", data)
        # 测试创建条目操作（年份失败）
        # response = self.client.post(
        #     "/", data=dict(title="New Movie2", year="123", follow_redirects=True)
        # )
        # data = response.get_data(as_text=True)
        # self.assertIn("创建成功", data)
        # self.assertIn("New Movie2", data)

    # 测试更新条目
    def test_edit_item(self):
        self.login()

        # 测试更新界面
        response = self.client.get("/movie/edit/1")
        data = response.get_data(as_text=True)
        self.assertIn("Edit item", data)
        # self.assertIn("Test Movie Title", data)
        self.assertIn("2019", data)

        # 测试编辑界面
        response = self.client.post(
            "/movie/edit/1",
            data=dict(title="Edit Movie Title", year="2019"),
            follow_redirects=True,
        )
        data = response.get_data(as_text=True)
        self.assertIn("更新成功", data)
        self.assertIn("Edit Movie Title", data)

        response = self.client.post(
            "/movie/edit/1",
            data=dict(title="Edit Movie Title", year="20"),
            follow_redirects=True,
        )
        data = response.get_data(as_text=True)
        self.assertIn("更新失败", data)

    # 测试删除条目
    def test_delete_item(self):
        self.login()

        response = self.client.post("/movie/delete/1", follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn("删除成功", data)

    # 测试登录保护
    def test_login_protect(self):
        response = self.client.get("/")
        data = response.get_data(as_text=True)
        self.assertNotIn("Logout", data)
        self.assertNotIn("Settings", data)
        self.assertNotIn('<form method="post">', data)
        self.assertNotIn("Delete", data)
        self.assertNotIn("Edit", data)

    # 测试登录
    def test_login(self):
        response = self.client.post(
            "/login", data=dict(username="test", password="123"), follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertNotIn("登录成功", data)

        # 可以使用更多的限制条件测试登录

    # 测试登出
    def test_logout(self):
        self.login()
        response = self.client.get("/logout", follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn("退出账号", data)

    # 测试设置
    def test_settings(self):
        self.login()
        response = self.client.post(
            "/setting", data=dict(name="edit_name"), follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn("更新成功", data)

    # 测试初始化终端命令
    def test_init_db_command(self):
        result = self.runner.invoke(init)
        self.assertIn("添加完成", result.output)
        self.assertNotEqual(Movie.query.count(), 0)

    # 测试创建管理员命令
    def test_admin_command(self):
        db.drop_all()
        db.create_all()
        result = self.runner.invoke(
            args=["admin", "--username", "grey", "--password", "123456"]
        )

        self.assertIn("创建管理员", result.output)
        self.assertIn("完成创建", result.output)

    # 测试更新管理员命令
    def test_admin_update_command(self):
        result = self.runner.invoke(
            args=["admin", "--username", "grey", "--password", "123456"]
        )
        self.assertIn("更新管理员", result.output)
        self.assertIn("完成创建", result.output)


if __name__ == "__main__":
    unittest.main()
