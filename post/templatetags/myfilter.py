# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : myfilter.by
# @Software : PyCharm

from django.template import Library

register = Library()


@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)

