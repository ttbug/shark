# shark
项目预览：[www.ttbug.win](www.ttbug.win)

项目使用方法：

项目使用的python版本为3.5.2，django版本为1.10.6。建议使用virtualenv创建虚拟环境运行

安装并激活virtualvenv虚拟环境

```
$pip install virtualenv
$virtualenv -p python3 venv  #指定创建基于python3的虚拟环境venv
$source venv/bin/active
(venv)colin@colin$      #当前面出现venv时说明以激活虚拟环境，退出时执行deactivate，如无特别说明，接下                         #来的操作都是在此虚拟环境下
```



环境搭建好以后，就可以运行我们的项目了

```
git clone https://github.com/ttbug/shark.git
cd shark/blogproject
pip install -r requirements.txt    #安装需要的python包
python manage.py makemigrations
python manage.py migrate            #数据库迁移
python manage.py runserver        #就可以在127.0.0.1:8000访问网站了
```



