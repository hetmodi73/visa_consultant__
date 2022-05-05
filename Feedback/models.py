from django.db import models
from client.models import user
from django.urls import reverse
# Create your models here.

class feedback(models.Model):
    # FEED_ID=models.IntegerField(null=True)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='feedback', null=True, blank=True)
    choice1=(
        ('1','1'),
        ('1.5','1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
    RATINGS=models.CharField(max_length=25, choices=choice1, null=True, blank=True)
    COMMENT=models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse('feedback-view')
