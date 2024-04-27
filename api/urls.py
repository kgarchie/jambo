from django.urls import path
from .views import StatusView, CustomerView, BusinessView, BusinessCategoryView, AreaView, CountyView, SubCountyView, \
    WardView, get_customer_businesses, get_business_customers

app_name = 'api'

urlpatterns = [
    path('status/', StatusView.as_view(), name='status'),
    path('customer/', CustomerView.as_view(), name='customers'),
    path('customer/<str:customer_ulid>/', CustomerView.as_view(), name='customer'),
    path('customer/<str:customer_ulid>/businesses', get_customer_businesses, name='customer_business'),
    path('business/', BusinessView.as_view(), name='business'),
    path('business/<str:business_ulid>/', BusinessView.as_view(), name='business'),
    path('business/category/', BusinessCategoryView.as_view(), name='business_categories'),
    path('business/<str:business_ulid>/customers', get_business_customers, name='business_customers'),
    path('county/', CountyView.as_view(), name='counties'),
    path('county/<str:county_name>/', CountyView.as_view(), name='county'),
    path('county/<str:county_name>/subcounty/', SubCountyView.as_view(), name='subcounties'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/', SubCountyView.as_view(), name='subcounty'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/', WardView.as_view(), name='wards'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/<str:ward_name>/', WardView.as_view(), name='ward'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/<str:ward_name>/area/', AreaView.as_view(), name='areas'),
    path('county/<str:county_name>/subcounty/<str:subcounty_name>/ward/<str:ward_name>/area/<str:area_name>/', AreaView.as_view(), name='area'),
]
