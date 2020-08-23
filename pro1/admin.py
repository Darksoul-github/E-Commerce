from django.contrib import admin
from pro1.models import *

admin.site.site_title='Shop'
admin.site.site_header='Shop Administration'

class ShopInline(admin.TabularInline):
    model=Item
    extra=1
class ShopAdmin(admin.ModelAdmin):
    inlines=[ShopInline]

admin.site.register(SubCategory1)
admin.site.register(SubCategory2)
admin.site.register(Category,ShopAdmin)
admin.site.register(SpecProperty)
admin.site.register(SpecCategory)