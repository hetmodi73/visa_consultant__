from django.urls import path
from .views import *

urlpatterns=[
    path('service_form/', NewServiceView.as_view(), name='service_form'),
    path('view/', ListServiceView.as_view(), name='service-view'),
    path("update/<int:pk>", UpdateServiceView.as_view(), name="service-update"),
    path("detail/<int:pk>", DetailServiceView.as_view(), name="service-detail"),
    path("delete/<int:pk>", DeleteServiceView.as_view(), name="service-delete"),

]
