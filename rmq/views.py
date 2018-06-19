#coding:utf8 
import random
import time
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from rmq.models import Info_apply_rmq,Infoip
from rmq.models import Users
import json

import csv,codecs
def index(request):
    if request.method == 'GET':
        # 获取所有学生信息
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/rmq/login/')
        if Users.objects.filter(u_ticket=ticket).exists():
            stuinfos = Users.objects.all()
            return render(request, 'rmq/index.html', {'stuinfos': stuinfos})
        else:
            return HttpResponseRedirect('/rmq/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'rmq/login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        # 查询用户是否在数据库中
        if Users.objects.filter(u_email=email).exists():
            user = Users.objects.get(u_email=email)
            if check_password(password, user.u_password):
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 绑定令牌到cookie里面
                # response = HttpResponse()
                response = HttpResponseRedirect('/rmq/')
                #max_age 存活时间(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                # 存在服务端
                user.u_ticket = ticket
                user.save() #保存
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, 'rmq/login.html', {'error_message': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, 'rmq/login.html', {'error_message': '用户不存在'})

def regist(request):
    if request.method == 'GET':
        return render(request,'rmq/regist.html')
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()
        password = make_password(password).strip()
        email = request.POST.get('email').strip()
        if Users.objects.filter(u_name=name).exists():
            return render(request,'rmq/regist.html',{'error_message':'用户已存在'})
        if Users.objects.filter(u_email=email).exists():
            return render(request,'rmq/regist.html',{'error_message':'邮箱已注册'})
        else:
            Users.objects.create(u_name=name,u_password=password,u_email=email)
            return HttpResponseRedirect('/rmq/')


def logout(request):
    #if request == 'GET':

    response = HttpResponseRedirect('/rmq/login/')
    response.delete_cookie('ticket')
    return response

def rmq_apply(request):
    if request.method == 'GET':
        return render(request,'rmq/rmq_apply.html')

    if request.method == 'POST':
        users = Users.objects.get(u_name = request.POST.get('users'))
        infoip =Infoip.objects.get(infoip = request.POST.get('infoip'))
        rmq_name1 = request.POST.get('rmq_name')
        if Info_apply_rmq.objects.filter(rmq_name=rmq_name1).exists():
            return render(request,'rmq/rmq_apply.html',{'rmq_error_message':'队列已存在'})
        else:
            rmq_name1=request.POST.get('rmq_name')
            rmq_user1=request.POST.get('users')
            infoip1 = request.POST.get('info_ip')
            apply_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            rmq_vhost1 = request.POST.get('rmq_vhost')
            rmq_exchange1 = request.POST.get('rmq_exchange')
            rmq_comment1 = request.POST.get('rmq_comment')
            rmq_product1 = request.POST.get('rmq_product')
            rmq_product_user1 = request.POST.get('rmq_product_user')
            rmq_consume1 = request.POST.get('rmq_consume')
            rmq_consume_user1 = request.POST.get('rmq_consume_user')
            rmq_data = Info_apply_rmq.objects.create(rmq_name=rmq_name1,users=users,infoip=infoip,
                apply_time=apply_time1,rmq_vhost=rmq_vhost1,rmq_exchange=rmq_exchange1,
                rmq_comment=rmq_comment1,rmq_product=rmq_product1,
                rmq_product_user=rmq_product_user1,rmq_consume=rmq_consume1,
                rmq_consume_user=rmq_consume_user1
                )
            rmq_data.save()
            
            return HttpResponseRedirect('/rmq/rmq_apply_detail/')

def rmq_apply_detail(request):
    rmq_detail = Info_apply_rmq.objects.all()
    return render(request,'rmq/rmq_apply_detail.html',{'rmq_detail':rmq_detail})

def rmq_export(request):
    import csv
    response = HttpResponse(content_type = 'text_csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = "attachment;filename='all.csv'"
    writer = csv.writer(response)
    rmq_all = Info_apply_rmq.objects.all()
    writer.writerow(['队列名称','交换机','申请人','虚拟主机','生产方','生产方负责人','消费方','消费方负责人',
        '申请时间'])
    for rmq in rmq_all:
        writer.writerow([rmq.rmq_name,rmq.rmq_exchange,rmq.users,rmq.rmq_vhost,rmq.rmq_product,
            rmq.rmq_product_user,rmq.rmq_consume,rmq.rmq_consume_user,rmq.apply_time])
    return response

##RMQ申请审核、0：待审核 1：审核成功 3：审核失败
from django.http import JsonResponse
import paramiko
@csrf_exempt
def rmq_check(request):
    if request.method == 'GET':
        return render(request,'rmq/rmq_apply_detail.html/')
    if request.method == 'POST':
        id = request.POST.get('id')
        rmq_socket = paramiko.SSHClient()
        rmq_socket.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        rmq_socket.connect(hostname='66.98.116.19',username='root',
            password='2Ofjw5ayN4hx',port=29124)
        stdin,stdout,stderr = rmq_socket.exec_command('touch /tmp/test1.txt')
        result = stderr.read()
        rmq_socket.close()
        if result:
            Info_apply_rmq.objects.filter(id = id).update(rmq_status=3)
            check_dict = {'msg':'审核失败'}
        else:
            id = request.POST.get('id')
            Info_apply_rmq.objects.filter(id = id).update(rmq_status=1)
            check_dict = {'msg':'审核成功'}
    return JsonResponse(check_dict)

#显示某个队列的申请详情
@csrf_exempt
def rmq_detail(request):
    if request.method == 'GET':
        return render(request,'rmq/rmq_apply_detail.html/')
    if request.method == 'POST':
        rmq_name = request.POST.get('rmq_name')
        rmq_dict = Info_apply_rmq.objects.filter(rmq_name=rmq_name).values()[0]
    return JsonResponse(rmq_dict)

