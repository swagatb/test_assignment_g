from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.


from article import models


admin.site.site_header = "Article Admin"
admin.site.unregister(Group)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Article, ArticleAdmin)
