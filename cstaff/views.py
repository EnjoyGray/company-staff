from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Position
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

# Create your views here.

class IndexListView(ListView):
    model = Staff
    template_name = "cstaff/index.html"
    context_object_name = 'employers'
    # title_page = 'Головна сторінка'
    paginate_by = 30
    
    
class EmployersListView(ListView):
    model = Staff
    template_name = "cstaff/employers.html"
    context_object_name = 'employers'
    title_page = 'Головна сторінка'
    paginate_by = 30
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
    
class MProfilDetailView(DetailView):
    model = Staff
    template_name = "cstaff/profil.html"
    context_object_name = 'profil'
    
    

    

# def index(request):
#     return render(request, "cstaff/index.html")
   


