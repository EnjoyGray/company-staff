from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Position
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

# Create your views here.

class StaffListView(ListView):
    model = Staff
    template_name = "cstaff/index.html"
    context_object_name = 'workers'
    title_page = 'Головна сторінка'
    paginate_by = 30
    
    

# def index(request):
#     return render(request, "cstaff/index.html")
   


