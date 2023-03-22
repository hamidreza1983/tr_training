from django.contrib import admin
from .models import post

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date' # اعمال یک گزینه تاریخ در بالای دیتا بیس
    list_display = ('id','title', 'author', 'status', 'created_date', 'published_date', 'counted_viwes', 'image')# چه فیلد هایی از آن سطر در صفحه نمایش داده شوند
    list_filter = ('status', )# افزودن یک گزینه فیلتر بر اساس استتوس ها و یا هر فیلد دیگری
    search_fields = ('title', 'author' )# یک سرچ فیلد میگذارد که یک عبارت را مثلا در ستون تایتل ها سرچ میکند
    empty_value_display = '-empty-' # اگر فیلدی خالی بود خالی نشان نده و بجای آن عبارتش را نشان بده
    fields = ('title', 'content', 'published_date', 'author', 'status', 'image') # وقتی بر روی یک سطر کلیک میکنیم کدام بخش ها قابل تغییر باشند 
#admin.site.register(post, PostAdmin)

# Register your models here.
