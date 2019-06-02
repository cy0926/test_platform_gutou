### django manage常用命令
```
$ cd 到 想要创建django项目的目录下

# 创建项目
$ django-admin startproject xxxx

# 创建引用
$ cd xxxx
$ python manage.py startapp xxxx

# 运行项目
$ python manage.py runserver

# 生成数据库同步文件
$ python  manage.py migrate

# 创建超级管理员账号
$ python manage.py createsuperuser

# 运行django单元测试

$ python manage.py test


```

### django MTV 模型
```angular2html
* M：models, django 封装了ORM,免于直接操作数据库
* T：templates, django 自带语言模版，可以在HTML中处理数据的展示
* V：views, 在models 和 templates之间处理数据

```
