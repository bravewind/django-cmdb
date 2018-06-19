from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^rmq_apply/$',views.rmq_apply,name='rmq_apply'),
    url(r'^rmq_apply_detail/$',views.rmq_apply_detail,name='rmq_apply_detail'),
    url(r'^rmq_check/$',views.rmq_check,name='rmq_check'),
    url(r'^rmq_export/$',views.rmq_export,name='rmq_export'),
    url(r'^rmq_detail/$',views.rmq_detail,name='rmq_detail'),

]