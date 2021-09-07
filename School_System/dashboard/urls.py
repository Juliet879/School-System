from .views import home
from django.urls import path


urlpatterns = [
    path("dashboard",home,name="landing")
]