from django.contrib import admin
from .models import Business, BusinessCategory, Customer

# Register your models here.

admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(BusinessCategory)
