from django.shortcuts import render

# Create your views here.
def view_courses(request):
    return render(request,'courses.html',{})