from django.urls import path
from .views import register_event,event_list

urlpatterns = [
    path("register/",register_event,name="registerEvent"),
    path("event_list/",event_list,name="viewEvent"),

]