from django.urls import path
from .views import *

urlpatterns = [
    path('question_form/', NewQuestionView.as_view(), name='question_form'),
    path('view/', ListQuestionView.as_view(), name='question-view'),
    path("update/<int:pk>", UpdateQuestionView.as_view(), name="question-update"),
    path("detail/<int:pk>", DetailQuestionView.as_view(), name="question-detail"),
    path("delete/<int:pk>", DeleteQuestionView.as_view(), name="question-delete"),

]
