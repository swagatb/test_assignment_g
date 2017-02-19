#!/usr/bin/env python
#coding:utf-8
"""
  Author: Swagat
  Purpose: Render default context data
  Created: Sunday 19 February 2017
"""

from article.models import Article


def what_next(request):
    return {"random_articles": Article.objects.get_random(4),}
