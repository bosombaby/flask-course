# 一、前言
Flask 是一个使用 Python 编写的轻量级 Web 应用框架。它基于 Werkzeug WSGI 工具箱和 Jinja2 模板引擎，提供了简单易用的 API，可以帮助开发者快速构建 Web 应用程序。Flask 框架具有灵活性和可扩展性，可以根据需要添加各种插件和扩展，例如数据库集成、表单验证、用户认证等。Flask 框架还提供了丰富的文档和社区支持，使得开发者可以轻松地学习和使用它。

![4.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1692609583997-1727dc21-f64f-4726-8895-e4697a4a592f.png#averageHue=%23f5f4f2&clientId=u104d5310-6296-4&from=ui&id=u483a6e2b&originHeight=870&originWidth=945&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=58857&status=done&style=none&taskId=u57ee62ab-0c8b-47d7-aa9b-c14683480af&title=)
**项目源码**：[flask-course](https://github.com/bosombaby/flask-course)
# 二、资源收集
## 2.1 在线教程
**官网**
[GitHub - pallets/flask: The Python micro framework for building web applications.](https://github.com/pallets/flask)

**中文教程**
[Flask 入门教程](https://tutorial.helloflask.com/)
使用版本：

- flask 2.1.3
- python > 3.6
## 2.2 环境配置
[Flask--如何在pycharm中导入并运行flask项目_此生小会的博客-CSDN博客](https://blog.csdn.net/cckavin/article/details/83746927)
[pycharm设置保存时自动格式化代码（Auto Reformat Code）_pycharm保存自动格式化_粒米LALA的博客-CSDN博客](https://blog.csdn.net/qq_41906934/article/details/124631826)
[新手必会，pycharm的调试功能(史上最详篇)](https://zhuanlan.zhihu.com/p/62610785)
# 三、入门
[Flask 入门教程 - 第 2 章：Hello, Flask!](https://tutorial.helloflask.com/hello/)
[Flask 入门教程 - 第 3 章：模板](https://tutorial.helloflask.com/template/)
# 四、静态文件

[Flask 入门教程 - 第 4 章：静态文件](https://tutorial.helloflask.com/static/)
# 五、数据库

**虚拟数据生成**：[https://github.com/joke2k/faker](https://github.com/joke2k/faker)
[SQLAlchemy](https://www.sqlalchemy.org/)
SQLAlchemy是一个Python库，用于在Python应用程序中使用关系型数据库。它提供了一组工具和API，使得在Python中使用关系型数据库变得更加容易和灵活。
SQLAlchemy的主要特点包括：

- ORM支持：SQLAlchemy提供了一个ORM(Object-Relational Mapping)框架，使得在Python中使用关系型数据库变得更加容易和直观。
- 多数据库支持：SQLAlchemy支持多种关系型数据库，包括MySQL、PostgreSQL、Oracle、Microsoft SQL Server等。
- 事务支持：SQLAlchemy支持完整的事务性，包括ACID属性(原子性、一致性、隔离性和持久性)。
- 数据库连接池：SQLAlchemy提供了一个数据库连接池，可以管理数据库连接的创建和销毁，从而提高应用程序的性能和可伸缩性。
- SQL表达式语言：SQLAlchemy提供了一个SQL表达式语言，使得在Python中编写SQL语句变得更加容易和安全。

使用SQLAlchemy，您可以在Python应用程序中轻松地执行各种数据库操作，包括创建、读取、更新和删除数据。您可以使用ORM框架来映射Python对象和数据库表，从而使得在Python中操作数据库变得更加直观和易于维护。
# 六、模板优化
[Flask 入门教程 - 第 6 章：模板优化](https://tutorial.helloflask.com/template2/)

**核心：模板的继承**
# 七、表单
[Flask 入门教程 - 第 7 章：表单](https://tutorial.helloflask.com/form/)

- 默认和入口文件放在同一个文件夹下面
- 名称为templates
# 八、用户认证
[Flask 入门教程 - 第 8 章：用户认证](https://tutorial.helloflask.com/login/)
## 8.1 werkzeug

- Werkzeug 是一个 Python Web 工具库，提供了一些用于构建 Web 应用程序的基础组件，包括路由、请求和响应对象、中间件、调试工具等。
- Werkzeug 的设计目标是提供简单、灵活、可扩展的工具，以便开发人员可以根据自己的需求构建定制化的 Web 应用程序。
## 8.2 flask_login
Flask-Login 是一个 Flask 扩展，用于处理用户认证和会话管理。下面是一些 Flask-Login 的特点：

- 提供了一组用于处理用户登录、注销、记住用户等功能的工具和约定。
- 轻松地集成到 Flask 应用程序中，只需要安装扩展并进行简单的配置即可。
- 支持多种用户模型和认证方法，可以根据应用程序的需求进行定制。
- 处理用户会话和 cookie，以便在用户访问应用程序时自动登录或注销。
- 处理用户权限和角色，以便在应用程序中实现访问控制和权限管理。
- 处理用户会话的保护和安全，以防止会话劫持和其他安全问题。
- 处理用户密码的加密和验证，以确保用户密码的安全性。
- 处理用户记住登录状态的功能，以便在用户关闭浏览器后仍然保持登录状态。
# 九、代码测试
## 9.1 unittest
[unittest教程_w3cschool](https://www.w3cschool.cn/unittest/)

- unittest 是 Python 标准库中的一个单元测试框架，用于编写和运行单元测试。
- 单元测试是一种测试方法，用于测试代码中的最小可测试单元，通常是函数或方法。
- unittest 提供了一组用于编写和运行单元测试的工具和约定，包括测试用例、测试套件、测试运行器等。
- 使用 unittest 可以帮助开发人员编写更可靠、更健壮的代码，并确保代码的正确性和稳定性。
- unittest 还支持测试覆盖率、测试报告等高级功能，可以帮助开发人员更好地了解代码的测试情况。
## 9.2 coverage
![1.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1692608904333-aa9c1e24-0588-4c52-b66d-f0e408dcfaf3.png#averageHue=%23f9f8f7&clientId=u104d5310-6296-4&from=ui&id=u73ad2045&originHeight=629&originWidth=1553&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=64312&status=done&style=none&taskId=ud076015d-2ad5-42a5-bae2-ecd0732c82f&title=)

![2.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1692608910240-c175e695-bd3e-4859-a985-4a726b3347ce.png#averageHue=%23faf9f8&clientId=u104d5310-6296-4&from=ui&id=u9040aa12&originHeight=302&originWidth=788&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23411&status=done&style=none&taskId=u445e1c9b-09cf-4e80-b75c-15a8c7a82d8&title=)
[Python代码覆盖率工具coverage使用教程 - ☆星空物语☆ - 博客园](https://www.cnblogs.com/songzhenhua/p/13194232.html)

- 可以帮助开发人员了解哪些代码被测试覆盖，哪些代码没有被测试覆盖，以及测试用例的质量和完整性。
- 可以生成各种格式的测试覆盖率报告，包括 HTML 报告、XML 报告、JSON 报告等。
- 可以与多种测试框架集成，包括 unittest、pytest、nose 等。
- 可以计算语句、分支、函数和行覆盖率等多种覆盖率指标。
- 可以忽略指定的文件、目录、代码行等，以便更精确地计算覆盖率。
- 可以在命令行或配置文件中设置各种选项，以便更灵活地使用。
- 是一个开源工具，可以免费使用，并且有活跃的社区支持和维护。
# 十、代码重构
[Flask 入门教程 - 第 10 章：组织你的代码](https://tutorial.helloflask.com/organize/)

[python中遇到循环import即circular import的问题原理剖析及解决方案_幸福清风的博客-CSDN博客](https://blog.csdn.net/xun527/article/details/108637094)

在 Python 中，循环导入通常是指两个或多个模块相互导入，导致无法解析模块依赖关系的问题。这种情况通常会导致 ImportError 异常或其他奇怪的行为。为了避免循环导入，可以尝试以下几种方法：

1. 重构代码，将循环依赖关系消除。
2. 将导入语句移动到函数内部，以延迟导入。
3. 将导入语句移动到模块底部，以确保所有依赖项都已定义。
4. 使用绝对导入语法，以避免相对导入语法的问题。


