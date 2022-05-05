from django.contrib import admin
from .models import question

# Register your models here.

class showquestion(admin.ModelAdmin):
    list_display = ['client','QUESTION','ANSWER','POINTS','services']

admin.site.register(question,showquestion)
