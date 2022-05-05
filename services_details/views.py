from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import service_details

# Create your views here.

def service_details_form(request):
    return render(request, "services_details/service_details_form.html")

def service_details_list(request):
    return render(request, "services_details/service_details_list.html")

def service_details_detail(request):
    return render(request, "services_details/service_details_detail.html")

def service_details_confirm_delete(request):
    return render(request,"services_details/service_details_confirm_delete.html")

class NewService_detailsView(CreateView):
    model = service_details
    fields = '__all__'
    template_name = 'services_details/service_details_form.html'

class ListService_detailsView(ListView):
    model = service_details
    context_object_name = 'services'
    template_name = 'services_details/service_details_list.html'

class UpdateService_detailsView(UpdateView):
    model = service_details
    fields = '__all__'
    template_name = 'services_details/service_details_form.html'

class DetailService_detailsView(DetailView):
    model = service_details
    fields = '__all__'
    success_url = '/services/view'

class DeleteService_detailsView(DeleteView):
    model = service_details
    success_url = '/services/view'
