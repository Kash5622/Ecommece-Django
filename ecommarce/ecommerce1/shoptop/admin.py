from django.contrib import admin

# Register your models here.
from .models import product,contact_us,order

admin.site.register(product)
admin.site.register(contact_us)
admin.site.register(order)