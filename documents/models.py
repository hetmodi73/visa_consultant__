from django.db import models
from django.urls import reverse
from client .models import user
from services .models import service
from services_details.models import service_details

# Create your models here.

class document(models.Model):
    # DOCUMENT_ID=models.IntegerField(null=True)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='document', null=True, blank=True)
    DOCUMENT_NAME=models.CharField(max_length=20, null=True, blank=True)
    DOCUMENT_FILE=models.FileField(default="",upload_to="profile", blank=True,null=True)
    services=models.ForeignKey(service,on_delete=models.CASCADE, related_name='document', blank=True,null=True)

    def __str__(self):
        return f"{self.client}-{self.services}"

    def get_absolute_url(self):
        return reverse('document-view')
