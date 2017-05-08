from __future__ import unicode_literals # Python 2.x 지원
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Product(models.Model):
    title = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    def __str__(self):
        return self.title
