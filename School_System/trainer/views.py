from .forms import TrainerRegistrationForm
from django.shortcuts import render

# Create your views here.
def trainer_register(request):
    form = TrainerRegistrationForm()
    return render(request ,"register_student.html",{"form":form})
