from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('Product/', views.Product_list),
    path('Product/<int:idk>/',views.Product_details),
]
