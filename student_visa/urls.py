from django.urls import path
from student_visa.views import *

urlpatterns=[
    path('visa_form/', NewVisaView.as_view(),name="visa_form"),
    path('view/', ListVisaView.as_view(), name='visa-view'),
    path("update/<int:pk>", UpdateVisaView.as_view(), name="visa-update"),
    path("delete/<int:pk>", DeleteVisaView.as_view(), name="visa-delete"),
    path("detail/<int:pk>", DetailVisaView.as_view(), name="visa-detail")

]
