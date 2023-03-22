from django.contrib import admin
from .models import post, category


admin.site.register(category)
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('id','title', 'author', 'status')
    list_filter = ('status', )
    search_fields = ('title', 'author' )
    empty_value_display = '-empty-'
    fields = ('title', 'content', 'published_date', 'author', 'status', 'image', 'category') 

