from django.urls import path
from .views import StatusView, CustomerView

app_name = 'api'

urlpatterns = [
    path('status/', StatusView.as_view(), name='status'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('customer/<str:customer_ulid>/', CustomerView.as_view(), name='customer'),
]
