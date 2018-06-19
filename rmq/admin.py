from django.contrib import admin

# Register your models here.
from .models import Info_apply_rmq,Infoip,Users

admin.site.register(Info_apply_rmq)
admin.site.register(Infoip)
admin.site.register(Users)