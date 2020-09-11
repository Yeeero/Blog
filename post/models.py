from django.db import models
from tinymce.models import HTMLField
# from DjangoUeditor.models import UEditorField
# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name=u'类别名称')

    class Meta:
        db_table = 'category'
        verbose_name_plural = '类别'

    def __str__(self):
        return 'Category:%s' % self.cname


class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name='标签名称')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = '标签'

    def __str__(self):
        return 'Tag:%s' % self.tname


class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    content = HTMLField()   # 后端展示为富文本编辑器的字段
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'

    def __str__(self):
        return 'Post:%s' % self.title
