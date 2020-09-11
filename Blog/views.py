# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : views.by
# @Software : PyCharm

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World!')