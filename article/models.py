from __future__ import unicode_literals

from datetime import date
import random

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            help_text= "Category name")
    is_public = models.BooleanField(default=True,
                                    help_text= "Tick, if the category is public.")
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"    


class ArticleManager(models.Manager):
    def get_random(self, numder= 1, exclude_ids= []):
        """
          First get only articles which is open for public
        """
        ids = self.filter(publication_date__lte=date.today()
                          ).exclude(id__in = exclude_ids).values_list('id', flat=True)
        rids = random.sample(ids, numder)
        return self.filter(id__in = rids)


class Article(models.Model):

    objects = ArticleManager()

    title = models.CharField(max_length=1000, help_text = "The title of the article.")
    author = models.ForeignKey(User, help_text = "Author of the article.")
    publication_date = models.DateField(default= date.today,
                                        help_text = "Date when this article will be public")
    category = models.ForeignKey(Category, related_name= "article_category")
    hero = models.ImageField(upload_to= "hero/")
    article_img = models.ImageField(upload_to = "extra/", null = True, blank = True)
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
