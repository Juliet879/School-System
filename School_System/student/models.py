from django.db import models
# from phonenumber_fields.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    date_of_birth =  models.DateField()
    nations = [
            ("KENYAN","Kenyan"),
            ("RWANDAN","Rwandan"),
            ("UGANDAN","Ugandan"),
            ("SOUTH SUDANEESE","South Sudaneese"),
    ]
    nationality = models.CharField(max_length=15,choices=nations,default="Kenyan")
    classes = [
        ("LOVELACE","Lovelace"),
        ("ANITA_B","AnitaB"),
        ("LISALAB","LisaLab"),
    ]
    class_name = models.CharField(max_length=2,choices=classes,default="AnitaB")
    id_number = models.CharField(max_length=2)
    email = models.EmailField()
    admission_date = models.DateField()
    academic_year = models.IntegerField()
    class_name = models.CharField(max_length=12,choices=classes)
    room_number = models.PositiveSmallIntegerField()
    medical_report = models.FileField()
    guardian_name = models.CharField(max_length=40)
    # guardian_contact = models.
    profile_image = models.FileField()
    
    
