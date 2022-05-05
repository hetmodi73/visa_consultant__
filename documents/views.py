from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import document

# Create your views here.

def document_form(request):
    return render(request, "documents/document_form.html")

def document_list(request):
    return render(request, "documents/document_list.html")

def document_detail(request):
    return render(request, "documents/document_detail.html")

def document_confirm_delete(request):
    return render(request, "documents/document_confirm_delete.html")

class NewDocumentView(CreateView):
    model = document
    fields = '__all__'
    template_name = 'documents/document_form.html'

class ListDocumentView(ListView):
    model = document
    context_object_name = 'blog'
    template_name = 'documents/document_list.html'

class UpdateDocumentView(UpdateView):
    model = document
    fields = '__all__'
    template_name = 'documents/document_form.html'

class DetailDocumentView(DetailView):
    model = document
    fields = '__all__'
    success_url = '/documents/view'

class DeleteDocumentView(DeleteView):
    model = document
    success_url = '/documents/view'
