from django.urls import path
from .views import register_student,student_list

urlpatterns = [
    path("register/",register_student,name="registerStudent"),
    path("student_list/",student_list,name="viewStudents")

]