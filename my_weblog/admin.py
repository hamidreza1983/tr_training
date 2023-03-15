from django.contrib import admin
from .models import post, contact, cheap_package



@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date' # اعمال یک گزینه تاریخ در بالای دیتا بیس
    list_display = ('id','title', 'status', 'created_date')# چه فیلد هایی از آن سطر در صفحه نمایش داده شوند
    list_filter = ('status', )# افزودن یک گزینه فیلتر بر اساس استتوس ها و یا هر فیلد دیگری
    search_fields = ('title', )# یک سرچ فیلد میگذارد که یک عبارت را مثلا در ستون تایتل ها سرچ میکند
    empty_value_display = '-empty-' # اگر فیلدی خالی بود خالی نشان نده و بجای آن عبارتش را نشان بده
    fields = ('title', 'content', 'published_date') # وقتی بر روی یک سطر کلیک میکنیم کدام بخش ها قابل تغییر باشند 
#admin.site.register(post, PostAdmin)

@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('id','name', 'email', 'subject', 'created_date')
    search_fields = ('subject', )
    list_filter = ('email', )

@admin.register(cheap_package)
class CheapAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['city', 'price','created_date']
    search_fields = ('city', )
    list_filter = ('price', )