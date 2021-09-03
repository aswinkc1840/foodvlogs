from django.contrib import admin

# Register your models here.
from shop.models import categ, product


class categadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(categ,categadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display = ['name', 'slug','price','img','desc']
    list_editable = ['price','img','desc']
admin.site.register(product,prodadmin)
