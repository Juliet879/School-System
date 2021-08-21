from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=40)
    organizer = models.CharField(max_length=35,null=True,blank=True)
    guest = models.CharField(max_length=35,null=True,blank=True)
    date = models.DateTimeField(max_length=10)
    event_description = models.TextField(null=True,blank=True)
    time_start = models.DateTimeField()
    end_time =models.DateTimeField()
    event_link = models.CharField(max_length=250,null=True,blank=True)