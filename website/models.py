from django.db import models
from django.urls import reverse

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default=None)
    zipcode = models.CharField(max_length=20)



    def __str__(self):
        return f"{self.first_name} {self.last_name} from {self.country}"
    

    def get_absolute_url(self):
        return reverse('record', kwargs={'pk': self.pk})