from django.db import models
from django.urls import reverse
from client.models import user
# Create your models here.

class service(models.Model):
    # SERVICE_ID=models.IntegerField(null=True)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='service', null=True, blank=True)
    choice=(
        ('IELTS Inquiry','IELTS Inquiry'),
        ('Immigration Visa', 'Immigration Visa'),
        ('Non-Immigration Visa', 'Non-Immigration Visa'),
        ('Visitor Visa', 'Visitor Visa'),
        ('Student Visa', 'Student Visa'),
        ('Business Visa', 'Business Visa'),
        ('Permanent Residence', 'Permanent Residence')

    )
    SERVICE_NAME=models.CharField(max_length=25, choices=choice, null=True, blank=True)

    def __str__(self):
        return f"{self.client}-{self.SERVICE_NAME}"

    def get_absolute_url(self):
        return reverse('service-view')


