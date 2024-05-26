from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Staff, Position
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

# Create your views here.

class IndexListView(ListView):
    model = Position
    template_name = "cstaff/index.html"
    context_object_name = 'positions'
    title_page = 'Home'

    def get_queryset(self):
        return Position.objects.filter(positionID__in=[1, 2, 3, 4])
    
    
class EmployersListView(ListView):
    model = Staff
    template_name = "cstaff/employers.html"
    context_object_name = 'employers'
    title_page = 'Employers'
    paginate_by = 25
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']
        context['page_range'] = paginator.get_elided_page_range(page_obj.number)
        return context
    
    
class SearchResultsView(ListView):
    model = Staff
    template_name = 'cstaff/search_results.html'
    context_object_name = 'employers'
    paginate_by = 25
    
    def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                if query.isdigit():  # Перевіряємо, чи введено числове значення для ID
                    return Staff.objects.filter(id=int(query))
                else:
                    return Staff.objects.filter(
                        Q(name__icontains=query) |
                        Q(position__position_staff__icontains=query) |
                        Q(date_of_employment__icontains=query)
                    )
            return Staff.objects.all()
        
    
class MProfilDetailView(DetailView):
    model = Staff
    template_name = "cstaff/profil.html"
    context_object_name = 'profil'
    
    

    

# def index(request):
#     return render(request, "cstaff/index.html")
   

