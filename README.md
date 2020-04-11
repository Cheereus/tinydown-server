# tinydown-server

tinydown server based on Django

## 环境和依赖

Anaconca3 (Python 3.7.1)

pip 20.0.2

Django 3.0.5

## 运行

```shell
python manage.py runserver
```

## 修改模型文件后需要同步数据库

首先为模型的改变生成迁移文件

```shell
python manage.py makemigrations
```

然后应用数据库迁移

```shell
python manage.py makemigrations
```
