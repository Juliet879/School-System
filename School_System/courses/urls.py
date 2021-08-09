from django.urls import path
from .views import view_courses


urlpatterns = [
    path('view_courses/',view_courses,name='courses_overview')
]