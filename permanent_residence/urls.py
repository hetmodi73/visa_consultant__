from django.urls import path
from .views import *

urlpatterns=[
    path('permanent_resi_form/', NewPermanent_resiView.as_view(), name="permanent_resi_form"),
    path('view/', ListPermanent_resiView.as_view(), name='permanent_resi-view'),
    path("update/<int:pk>", UpdatePermanent_resiView.as_view(), name="permanent_resi-update"),
    path("delete/<int:pk>", DeletePermanent_resiView.as_view(), name="permanent_resi-delete"),
    path("detail/<int:pk>", DetailPermanent_resiView.as_view(), name="permanent_resi-detail")

]
