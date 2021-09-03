from django.contrib import admin

# Register your models here.
from cart.models import cartlist, item

admin.site.register(cartlist)
admin.site.register(item)