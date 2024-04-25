from django.urls import path
from .views import Status

app_name = 'api'

urlpatterns = [
    path('status/', Status.as_view(), name='status')
]
