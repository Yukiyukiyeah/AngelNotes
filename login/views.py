# coding=utf-8
import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import random
import json
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import sys
from login.models import Math

path = os.path.dirname(os.path.realpath(__file__))
log_path = path + os.sep + 'log' + os.sep


def index(request):
    pass
    return render(request, "index.html")


# 用户注册
@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
            return render(request, 'register.html', {'errors': errors})
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
            return render(request, 'register.html', {'errors': errors})
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('确认一下你的密码吧')
            return render(request, 'register.html', {'errors': errors})
        else:
            password2 = request.POST.get('password2')
        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入的密码不一致')

        if account is not None and password is not None and password2 is not None and CompareFlag:
            ss = User.objects.filter(username=account).count()
            if ss > 0:
                errors.append("该用户名已经存在")
                return render(request, 'register.html', {'errors': errors})
            user = User.objects.create_user(account, email, password)
            user.save()
            userlogin = auth.authenticate(username=account, password=password)
            auth.login(request, userlogin)
            return redirect('/login/')
    return render(request, 'register.html', {'errors': errors})


# 用户登录
@csrf_exempt
def my_login(request):
    global whichAngel
    errors = []
    account = None
    password = None
    if request.method == "POST":
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if account is not None and password is not None:
            user = auth.authenticate(username=account, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("account:", account)
                    whichAngel = account
                    if account == 'zhoulaoshi':
                        report = readLog()
                        return render(request, 'summary.html', {'report': report})
                    return redirect('/index/')
                else:
                    errors.append('用户名错误')
            else:
                errors.append('用户名或密码错误')
    return render(request, 'login.html', {'errors': errors})


# 用户退出
def my_logout(request):
    auth.logout(request)
    return redirect("/login/")


# @login_required
def test(request):
    return render(request, 'testMath.html', {"whichAngel": whichAngel})


def generateTest():
    test_list = []
    n1 = random.randint(11, 100)
    n2 = random.randint(10, n1 - 1)
    s_p = '{0} + {1} ='.format(n1, n2)
    s_m = '{0} - {1} ='.format(n1, n2)
    if n1 % 2 == 0:
        s = s_p
        r_answer = n1 + n2
    else:
        s = s_m
        r_answer = n1 - n2
    test_list.append(s)
    test_list.append(r_answer)
    return test_list


def answer(request):
    result = json.loads(str(request.body, 'utf-8'))
    result = str(result).replace("'", '"')
    print(result)
    result.encode('UTF-8')
    saveLog(result)
    return HttpResponse('true')


def saveLog(log):
    current = whichAngel + '-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    with open(path + os.sep + 'log' + os.sep + current + '.json', 'wb') as f:
        try:
            f.write(log.encode(encoding='UTF-8'))
        except Exception as e:
            print("encoding:", sys.getdefaultencoding())
            print("my error:", e)
        else:
            f.close()


def summary(request):
    return render(request, 'summary.html')


def readLog():
    report = []
    list_log = os.listdir(log_path)
    current = datetime.datetime.now().strftime('%Y-%m-%d')
    date_time = ''
    for i in list_log:
        print(i)
        with open(log_path + i, 'rb') as f:
            content = json.load(f)
            if current == content['date']:
                record = content['date'] + ':   ' + content['whichAngel'] + "今天完成" + str(
                    content['total']) + "道题，做对了" + str(
                    content['score']) + "道，做错" + str(content['lost']) + "道."
                report.append(record)
            else:
                continue
    print(report)
    return report
