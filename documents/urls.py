from django.urls import path
from .views import *

urlpatterns = [
    path('document_form/', NewDocumentView.as_view(), name='document_form'),
    path('view/', ListDocumentView.as_view(), name='document-view'),
    path("update/<int:pk>", UpdateDocumentView.as_view(), name="document-update"),
    path("detail/<int:pk>", DetailDocumentView.as_view(), name="document-detail"),
    path("delete/<int:pk>", DeleteDocumentView.as_view(), name="document-delete"),

]
