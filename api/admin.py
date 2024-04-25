from django.contrib import admin
from .models import Business, BusinessCategory, Contact, Customer

# Register your models here.

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Business)
admin.site.register(BusinessCategory)
