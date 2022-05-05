from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import question

# Create your views here.

def question_form(request):
    return render(request, "questions/question_form.html")

def question_list(request):
    return render(request, "questions/question_list.html")

def question_detail(request):
    return render(request, "questions/question_detail.html")

def question_confirm_delete(request):
    return render(request, "questions/question_confirm_delete.html")

class NewQuestionView(CreateView):
    model = question
    fields = '__all__'
    template_name = 'questions/question_form.html'

class ListQuestionView(ListView):
    model = question
    context_object_name = 'blog'
    template_name = 'questions/question_list.html'

class UpdateQuestionView(UpdateView):
    model = question
    fields = '__all__'
    template_name = 'questions/question_form.html'

class DetailQuestionView(DetailView):
    model = question
    fields = '__all__'
    success_url = '/questions/view'

class DeleteQuestionView(DeleteView):
    model = question
    success_url = '/questions/view'
