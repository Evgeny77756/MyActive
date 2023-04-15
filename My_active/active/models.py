from django.db import models
from django.urls import reverse

class Stock(models.Model):
    name = models.CharField(max_length=100)
    data_open = models.DateField(null=True, blank=True)
    price = models.FloatField(null=True, default=0)
    image = models.ImageField(null=True, upload_to='stock/images/')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('action-detail', args=[str(self.id)])



