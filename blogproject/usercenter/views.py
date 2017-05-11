from django.shortcuts import render
from django.contrib.auth.models import User
import uuid
import datetime
from django.utils import timezone
from django.core.mail import send_mail
from .models import ActivateCode
# Create your views here.


def register(request):
    err = ''
    if request.method == "GET":
        return render(request, "usercenter/register.html")
    else:
        name = request.POST['username'].strip()
        passwd = request.POST['passwd'].strip()
        re_passwd = request.POST['re_passwd'].strip()
        email = request.POST['email'].strip()

        if not name or not passwd or not re_passwd or not email:
            err = "字段均不能为空"
            return render(request, 'usercenter/register.html', {'msg': err})

        if passwd != re_passwd:
            err = "两次密码输入不一致，请重新输入"
            return render(request, 'usercenter/register.html', {'msg': err})

        if len(passwd) < 8:
            err = "密码长度必须大于8"
            return render(request, 'usercenter/register.html', {'msg': err})

        if User.objects.filter(username=name).count() > 0:
            err = "用户名已存在"
            return render(request, 'usercenter/register.html', {'msg': err})

        if User.objects.filter(email=email).count() > 0:
            err = "当前邮箱已经注册"
            return render(request, "usercenter/register.html", {'msg': err})

        user = User.objects.create_user(name, email, passwd)
        user.is_active = False
        user.save()
        # 生成激活码
        new_code = str(uuid.uuid4()).replace('-', '')
        # 设置激活码过期时间
        expire_time = timezone.now() + datetime.timedelta(days=2)

        code_record = ActivateCode(user=user, code=new_code, expire_timestamp=expire_time)
        code_record.save()

        activate_link = "http://%s/usercenter/activate/%s" % (request.get_host(), new_code)
        activate_email = '''点击<a href="%s">这里</a>激活''' % activate_link

        send_mail(subject='[Bazinga]激活邮件',
                message='点击链接激活%s' % activate_link,
                html_message=activate_email,
                from_email='1137048513@qq.com',
                recipient_list=[email],
                fail_silently=False,
            )

        return render(request, "usercenter/register_success.html", {"msg": "注册成功，请前往邮箱激活"})


def activate(request, code):
    # 找到注册时创建的实例
    acts = ActivateCode.objects.filter(code=code, expire_timestamp__gte=timezone.now())
    print(acts)
    if acts.count() > 0:
        code_record = acts[0]
        code_record.user.is_active = True
        code_record.save()
        return render(request, "usercenter/activate_status.html", {'msg': "激活成功"})
    return render(request, "usercenter/activate_status.html", {'msg': "激活失败"})
