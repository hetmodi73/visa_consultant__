from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import service
# Create your views here.

def service_form(request):
    return render(request, "services/service_form.html")

def service_list(request):
    return render(request, "services/service_list.html")

def service_detail(request):
    return render(request, "services/service_detail.html")

def service_confirm_delete(request):
    return render(request, "services/service_confirm_delete.html")

class NewServiceView(CreateView):
    model = service
    fields = '__all__'
    template_name = 'services/service_form.html'

class ListServiceView(ListView):
    model = service
    context_object_name = 'services'
    template_name = 'services/service_list.html'

class UpdateServiceView(UpdateView):
    model = service
    fields = '__all__'
    template_name = 'services/service_form.html'

class DetailServiceView(DetailView):
    model = service
    fields = '__all__'
    success_url = '/services/view'

class DeleteServiceView(DeleteView):
    model = service
    success_url = '/services/view'
