#coding:utf8
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
	u_name = models.CharField(max_length=20)
	u_password = models.CharField(max_length=20)
	u_email = models.CharField(max_length=25,default=True)
	u_ticket = models.CharField(max_length=30, null=True)


	def __str__(self):
		return self.u_name

	class Meta:
		db_table = 'rmq_user'

class Infoip(models.Model):
	IP_ZONE = (
		('aliyun','Aliyun'),
		('AWS','AWS'),
		('commany_inter','commany_inter'),
		)
	ip_zone = models.CharField(max_length=10,choices=IP_ZONE)
	infoip = models.CharField(max_length=100)
	def __str__(self):
		return self.infoip

class Info_apply_rmq(models.Model):
	#队列名称
	rmq_name = models.CharField(max_length=100)
	#队列申请人名称
	users = models.ForeignKey(Users)
	#申请的IP地址
	infoip = models.ForeignKey(Infoip)
	#队列的状态
	rmq_status = models.IntegerField(max_length=1,default=0)
	#申请的时间
	apply_time = models.DateTimeField()
	#申请的rabbitmq的vhost
	rmq_vhost = models.CharField(max_length=20)
	#申请的交换机名称
	rmq_exchange = models.CharField(max_length=50)
	#队列描述
	rmq_comment = models.CharField(max_length=200)
	#队列生产方
	rmq_product = models.CharField(max_length=20)
	#生产方负责人
	rmq_product_user = models.CharField(max_length=20)
	#队列消费方
	rmq_consume = models.CharField(max_length=20)
	#队列消费方负责人
	rmq_consume_user = models.CharField(max_length=20)

	def __str__(self):
		return self.rmq_name


