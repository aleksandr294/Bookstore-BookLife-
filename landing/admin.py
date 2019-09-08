from django.contrib import admin
from .models import *
# Register your models here.



class SubscribersAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'password']
    list_filter=('name',)
    search_fields=['name']
    class Meta:
        model=Subscribers
admin.site.register(Subscribers, SubscribersAdmin)