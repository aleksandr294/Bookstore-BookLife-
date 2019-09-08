from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Product._meta.fields]
    search_fields=['name_book', 'author', 'publishing' ]
    class Meta:
        model=Product

admin.site.register(Product, ProductAdmin)



