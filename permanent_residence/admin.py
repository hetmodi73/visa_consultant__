from django.contrib import admin
from .models import permanent_resi

# Register your models here.

class showpermanent_resi(admin.ModelAdmin):
    list_display = ['SKILLED_EMPLOYMENT','WORK_EXPERIENCE','QUALIFICATIONS','AGE_20TO55_YEARS','Skilled_employment_2','Work_experience_2','Additional_Bonus_Points','QUALIFICATIONS_2','Partner_Qualifications','client','text','city','resume']

admin.site.register(permanent_resi,showpermanent_resi)
