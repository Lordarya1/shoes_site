from django.urls import path
from .views import ss

app_name='stepapp'
urlpatterns=[
    path('',ss)
]