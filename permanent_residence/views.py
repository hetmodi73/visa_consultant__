from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import permanent_resi

# Create your views here.

def permanent_resi_form(request):
    return render(request,"permanent_residence/permanent_resi_form.html")

def permanent_resi_list(request):
    return render(request, "permanent_residence/permanent_resi_list.html")

class NewPermanent_resiView(CreateView):
    model = permanent_resi
    fields = '__all__'
    template_name = 'permanent_residence/permanent_resi_form.html'

class ListPermanent_resiView(ListView):
    model = permanent_resi
    context_object_name = 'visa'
    template_name = 'permanent_residence/permanent_resi_list.html'

class UpdatePermanent_resiView(UpdateView):
    model = permanent_resi
    fields = '__all__'
    template_name = 'permanent_residence/permanent_resi_form.html'

class DetailPermanent_resiView(DetailView):
    model = permanent_resi
    fields = '__all__'
    success_url = '/permanant_residence/view'

class DeletePermanent_resiView(DeleteView):
    model = permanent_resi
    success_url = '/permanant_residence/view'
