from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import visa
# Create your views here.

def visa_form(request):
    return render(request,"student_visa/visa_form.html")

def visa_list(request):
    return render(request, "student_visa/visa_list.html")

class NewVisaView(CreateView):
    model = visa
    fields = '__all__'
    template_name = 'student_visa/visa_form.html'

class ListVisaView(ListView):
    model = visa
    context_object_name = 'visa'
    template_name = 'student_visa/visa_list.html'

class UpdateVisaView(UpdateView):
    model = visa
    fields = '__all__'
    template_name = 'student_visa/visa_form.html'

class DetailVisaView(DetailView):
    model = visa
    fields = '__all__'
    success_url = '/student_visa/view'

class DeleteVisaView(DeleteView):
    model = visa
    success_url = '/student_visa/view'
