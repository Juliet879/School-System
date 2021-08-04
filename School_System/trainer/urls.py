from django.urls import path
from .views import trainer_register

urlpatterns =[
    path('register',trainer_register,name="registerTrainer")
]