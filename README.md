## NJVS(南京理工大学青年志愿者平台)

## 简介

​	平台依旧是基于Django,后台采用了xamdin来搭建,效果比原生的admin管理界面更加优美。

## 环境搭建

1.在虚拟环境下

```shell
pip install -r requirements.txt

Pillow 若安装失败尝试执行

sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
```

2.安装redis

```shell
sudo apt-get install redis-server
```

3.在项目根目录下新建config文件,并在文件中新建mysql.conf配置数据库,mysql.cofig模板如下

```
{
    "USER" : "root",
    "PASSWORD" : "123456",
    "HOST" : "localhost"
}
```

4.新建名为njvs的数据库

5.执行 ```python manage.py runserver 0.0.0.0:8000```



