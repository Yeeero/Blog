# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : search_indexes.by
# @Software : PyCharm

from haystack import indexes
from post.models import *


# 格式：模型类名+Index
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    # 给搜索字段设置索引：title，content
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')