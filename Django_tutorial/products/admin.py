from django.contrib import admin
from .models import Products,UserModel
from .models import BookData
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')

# class OfferAdmin(admin.ModelAdmin):
#     list_display=('code','discount')

class UserModelAdmin(admin.ModelAdmin):
    list_display=('username','password','email')

# Register your models here.
admin.site.register(Products,ProductAdmin)
# admin.site.register(Offer,OfferAdmin)
admin.site.register(UserModel,UserModelAdmin)






@admin.register(BookData)
class BookDataAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'book_price', 'show_image')
    search_fields = ('book_name', 'book_author', 'book_price')
    list_filter = ('book_author',)
    ordering = ('book_name',)
    list_editable = ('book_author', 'book_price')
    

    def show_image(self, obj):
        if obj.book_image:
            return format_html('<img src="{}" width="50" height="70" />', obj.book_image.url)
        return "No Image"
    show_image.short_description = "Book Cover"