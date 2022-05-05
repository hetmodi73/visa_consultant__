from django.db import models
from django.urls import reverse
from client .models import user
from services .models import service
from services_details.models import service_details

# Create your models here.

class question(models.Model):
    # QUESTION_ID=models.IntegerField(null=True)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='master_question', null=True, blank=True)
    QUESTION=models.CharField(max_length=50, null=True, blank=True)
    ANSWER=models.CharField(max_length=50, null=True, blank=True)
    POINTS=models.IntegerField(null=True, blank=True)
    services=models.ForeignKey(service_details,on_delete=models.CASCADE, related_name='master_question', blank=True,null=True)

    def __str__(self):
        return f"{self.client}-{self.services}"

    def get_absolute_url(self):
        return reverse('question-view')
