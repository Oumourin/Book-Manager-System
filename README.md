#  图书管理系统

##  中北大学数据库课程设计作业

###  项目介绍

本项目基于Python3.x和Flask开发，前端使用Bootstrap构建，DBMS采用MySQL8（也可自行选择其他DBMS，具体方法参考SQLAlchemy文档），本项目支持使用Docker部署，并已预编写Dockerfile

###  使用方法

####  开发

debug模式下，使用run-development.py运行，调试前请手动向数据库提交一个用户账户信息

```python
from book import db
from book.model import Operator
db.create_all()
default = Operator('test', 'test@test.com', 'test123')
default.set_password()
db.session.add(default)
db.session.commit()

```

上述代码将会向数据库提交一个用户名为test邮箱为test@test.com密钥为test123的用户

####  部署

生产环境下，使用run-development.py运行，系统将会自动创建一个用户名为test邮箱为test@test.com密钥为test123的用户

####  Docker

```dockerfile
docker run -name <镜像名> -p 8080:8080 -d <容器名>
```



以上命令会创建一个运行在8080端口的本项目，具体部署细节请参考Docker官方文档

###  本项目的坑

+ 前端Form有一些缺少判断规则
+ 库存管理尚未完成
+ 没有用户注册逻辑（当时是考虑到实际应用场景，SHA256加密是之后加的功能）

###   最后

本项目仅仅作为一个课程设计作业，给具有类似课设的同学一个参考