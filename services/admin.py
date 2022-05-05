from django.contrib import admin
from .models import service
# Register your models here.

class showservice(admin.ModelAdmin):
    list_display = ['client','SERVICE_NAME']

admin.site.register(service,showservice)
