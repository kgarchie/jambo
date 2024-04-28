from django.urls import path
from .views import StatusView, CustomerView, BusinessView, BusinessCategoryView, AreaView, CountyView, SubCountyView, \
    WardView, get_customer_businesses, get_business_customers, get_nationalities, send_data_deletion_link, delete_customer

app_name = 'api'

urlpatterns = [
    path('status', StatusView.as_view(), name='status'),
    path('customers', CustomerView.as_view(), name='customers'),
    path('customer/<str:customer_ulid>', CustomerView.as_view(), name='customer'),
    path('customer/<str:customer_ulid>/businesses', get_customer_businesses, name='customer_business'),
    path('customer/<str:customer_ulid>/delete/request', send_data_deletion_link, name='request_delete_customer'),
    path('customer/<str:token>/delete/confirm', delete_customer, name='confirm_delete_customer'),
    path('businesses', BusinessView.as_view(), name='businesses'),
    path('business/<str:business_ulid>', BusinessView.as_view(), name='business'),
    path('business_categories', BusinessCategoryView.as_view(), name='business_categories'),
    path('business/<str:business_ulid>/customers/', get_business_customers, name='business_customers'),
    path('counties', CountyView.as_view(), name='counties'),
    path('county/<str:county_name>', CountyView.as_view(), name='county'),
    path('county/<str:county_name>/subcounties', SubCountyView.as_view(), name='subcounties'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>', SubCountyView.as_view(), name='subcounty'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/wards', WardView.as_view(), name='wards'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/<str:ward_name>', WardView.as_view(), name='ward'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/<str:ward_name>/areas', AreaView.as_view(), name='areas'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/<str:ward_name>/area/<str:area_name>', AreaView.as_view(), name='area'),
    path('nationalities/', get_nationalities, name='nationalities'),
]
