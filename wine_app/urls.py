from django.urls import path
from .views import BottleList

urlpatterns: [
    path('', BottleList.as_view(), name='bottle_list')
]