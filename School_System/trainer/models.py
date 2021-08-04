from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    company    = models.CharField(max_length=20)
    course   = models.CharField(max_length=30)
    gender_choices   = [
        ('Female','Female'),
        ('Male', 'Male')
    ]
    gender = models.CharField(max_length=6,choices=gender_choices)
    joining_date = models.DateField()
    salary = models.BigIntegerField()
    city = models.CharField(max_length=12)
    image = models.FileField()
    resume = models.FileField()
    contract = models.FileField()