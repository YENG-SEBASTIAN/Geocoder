from django.db import models

# Create your models here.

class SearchAddress(models.Model):
    place_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.place_name