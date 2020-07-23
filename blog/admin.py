from django.contrib import admin
from blog import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'count_post')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
