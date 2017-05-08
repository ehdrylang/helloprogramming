from django.contrib import admin
from hp.models import Product
# Register your models here.
# admin 페이지에 등록하기
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','nation')

admin.site.register(Product,ProductAdmin)
