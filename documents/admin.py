from django.contrib import admin
from .models import document

# Register your models here.

class showdocument(admin.ModelAdmin):
    list_display = ['client','DOCUMENT_NAME','DOCUMENT_FILE','services']

admin.site.register(document,showdocument)
