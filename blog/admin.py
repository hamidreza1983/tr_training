from django.contrib import admin
from .models import post, category, comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('id','title', 'author', 'status')
    list_filter = ('status', )
    search_fields = ('title', 'author' )
    empty_value_display = '-empty-'
    fields = ('title', 'content', 'published_date', 'author', 'status', 'image', 'category', 'tags')
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email', 'status', 'created_date')
    list_filter = ('status', )
    search_fields = ('name', 'email' )
    empty_value_display = '-empty-'
    fields = ('post', 'name','email', 'status', 'subject', 'text')

admin.site.register(post, PostAdmin)
admin.site.register(category)
admin.site.register(comment, CommentAdmin)

     

