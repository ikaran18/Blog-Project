from django.contrib import admin
from .models import cartoon,Category,contact
# Register your models here.
admin.site.register(cartoon)
admin.site.register(Category)
admin.site.register(contact)


# @admin.register(cartoon)
# class cartoonAdmin(admin.ModelAdmin):
#     list_display=('id','card_title','image','description')
    
    
# admin.site.register(cartoon,cartoonAdmin)
