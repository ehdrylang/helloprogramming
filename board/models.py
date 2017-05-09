from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE',max_length=100)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True,help_text='별칭')
    description = models.CharField('DESCRIPTION',max_length=100,blank=True,help_text='간단한 소개')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date',auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date',auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'board' #디비 테이블명 지정
        ordering = ('-modify_date',) # 최근수정일순

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',arg=(self.slug,))
    def get_previous_post(self):
        return self.get_previous_by_modify_date()
    def get_next_post(self):
        return self.get_next_by_modify_date()
