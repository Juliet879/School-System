from django.urls import path
from .views import trainer_register,trainer_list

urlpatterns =[
    path('register',trainer_register,name="registerTrainer"),
    path('trainer_list',trainer_list,name="trainerList")
]