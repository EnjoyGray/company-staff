from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# class StaffListView(ListView):
#     model = Staff
#     template_name = ".html"

def index(request):
    return render(request, "cstaff/index.html")
   