# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : mycontextprocessor.by
# @Software : PyCharm
from django.db.models import Count
from django.db import connection

from post.models import Post


def getRightInfo(request):
    # 1获取分类信息
    r_category = Post.objects.values('category__cname', 'category_id', 'category').annotate(c=Count('*')).order_by('-c')
    # 2. 获取归档信息
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) c,created FROM t_post GROUP BY DATE_FORMAT(created, '%Y-%m') ORDER BY c DESC, created DESC")
        r_datalist = cursor.fetchall()
    # 3.获取文章
    r_recposts = Post.objects.all().order_by('-created')[:3]
    return locals()