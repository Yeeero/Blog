# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : views.by
# @Software : PyCharm
from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import render
from django.views.generic.base import View
from django.views.decorators.cache import cache_page    # 缓存第三方库

from post.models import Post


def index(request):
    pageNo = request.GET.get('num', 1)
    pageNo = int(pageNo)

    postlist = Post.objects.all().order_by('-created')
    paginator = Paginator(postlist, 1)
    pagelist = paginator.page(pageNo)
    return render(request, 'index.html', locals())


class IndexView(View):

    def get(self, request, num=1):
        postlist = Post.objects.all().order_by('-created')
        paginator = Paginator(postlist, 2)
        pagelist = paginator.page(num)
        return render(request, 'index.html', locals())


class PostView(View):

    def get(self, request, postid):
        post = Post.objects.get(pk=postid)
        return render(request, 'detail.html', locals())


@cache_page(20)	  # 设置缓存过期时间
def getArticleBy(request, categoryid=None, year=None, month=None):
    if categoryid:
        postlist = Post.objects.filter(category_id=categoryid).order_by('-created')
    elif year:
        postlist = Post.objects.filter(created__year=year,created__month=month)
        print(postlist)
    else:
        postlist = Post.objects.all().order_by('-created')
    # print(postlist)
    return render(request, 'article.html', locals())


# def getAricleByDate(request, date=None):
#     if date:
#         with connection.cursor() as cursor:
#             sql = '''
#                 SELECT * FROM t_post WHERE DATE_FORMAT(created, '%Y-%m')="{}"
#             '''.format(date)
#             cursor.execute(sql)
#             postlist = cursor.fetchall()
#             print(postlist)
#     else:
#         postlist = Post.objects.all().order_by('-created')
#     return render(request, 'article.html', locals())
