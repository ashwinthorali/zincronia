from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['h1']
    search_fields = ['title', 'h1', 'content','slug']


admin.site.register(Blog, BlogAdmin)

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tags)
