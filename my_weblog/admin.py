from django.contrib import admin
from .models import contact, cheap_package, luxary_package, camping_package, newsletter




    

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

@admin.register(luxary_package)
class LuxaryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['city', 'price','created_date']
    search_fields = ('city', )
    list_filter = ('price', )


@admin.register(camping_package)
class LuxaryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['city', 'price','created_date']
    search_fields = ('city', )
    list_filter = ('price', )

@admin.register(newsletter)
class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['email', 'created_date']
    search_fields = ('email', )
    list_filter = ('created_date', )