from django.contrib import admin
from .models import Business, BusinessCategory, Customer, County, Ward, SubCounty, Area

# Register your models here.

admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(BusinessCategory)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward)
admin.site.register(Area)