from django.urls import path
from .views import *

urlpatterns=[
    path('service_details_form/', NewService_detailsView.as_view(), name='service_details_form'),
    path('view/', ListService_detailsView.as_view(), name='service_details-view'),
    path("update/<int:pk>", UpdateService_detailsView.as_view(), name="service_details-update"),
    path("detail/<int:pk>", DetailService_detailsView.as_view(), name="service_details-detail"),
    path("delete/<int:pk>", DeleteService_detailsView.as_view(), name="service_details-delete")

]
