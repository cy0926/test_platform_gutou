### MYSQL 配置


参考：https://docs.djangoproject.com/en/2.1/ref/databases/
1、先需要有一个MySQL数据库，可以单独安装，也可以使用WampServer的集成环境
  -->WampServer包含了apache,phpAdmin,mysql
  
2、在项目根目录创建一个配置文件mysql.cnf
```mysql
[client]
host = 127.0.0.1
port = 3306
user = root
password = root
database = gutou_test_platform
default-character-set = utf8
```

3、 settings.py 添加mysql的配置：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BASE_DIR+'/mysql.cnf',
        },
    }
}
```

4、安装mysqlclient
```python
    pip install mysqlclient
```

5、重新执行数据库迁移和创建超级管理员账号的命令
```python
    python manage.py migrate
    python manage.py createsuperuser
```