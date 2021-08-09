from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        # tells the database it wants all the data in the database for chosen fields you put the fields in a tuple
        fields = "__all__"     
        widgets = {
            "first_name":forms.TextInput(attrs={'class':"form-control",'style':"width:70%"})
        }

