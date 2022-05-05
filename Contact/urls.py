from django.urls import path
from .views import *

urlpatterns = [
    path('contact_form/', NewContactView.as_view(), name = 'contact_form'),
    path('view/', ListContactView.as_view(), name= 'contact-view'),
    path("update/<int:pk>", UpdateContactView.as_view(), name="contact-update"),
    path("delete/<int:pk>", DeleteContactView.as_view(), name="contact-delete"),
    path("detail/<int:pk>", DetailContactView.as_view(), name="contact-detail")
]
