from django.urls import path
from .views import staff_register,staff_list,edit_staff,staff_profile,delete_staff



urlpatterns = [
    path("register_staff",staff_register,name="staffRegister"),
    path('stuff_list',staff_list,name="stuffList"),
    path('edit/<int:id>/',edit_staff,name="editStuff"),
    path('profile/<int:id>/',staff_profile,name="stuffProfile"),
    path('delete/<int:id>/',delete_staff,name="deleteStuff"),
]