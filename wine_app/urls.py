from django.urls import path
from .views import BottleList, BottleListDetail

urlpatterns = [
    path('', BottleList.as_view(), name='bottle_list'),
    path('<int:pk>/', BottleListDetail.as_view(), name='bottle_list'),
]