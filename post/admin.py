from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display =['title', 'desc', 'created']  # 设置显示哪些字段
    search_fields =['title']    # 添加搜索的字段
    list_per_page =5


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)


