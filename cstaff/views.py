from django.shortcuts import render
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
    
    
    
class MProfilDetailView(DetailView):
    model = Staff
    template_name = "cstaff/profil.html"
    context_object_name = 'profil'
    
    

    

# def index(request):
#     return render(request, "cstaff/index.html")
   


# {% for p in positions %}
#     <div class="positions">
#         <div class="mcard">
#             <div class="prof">
#                 {% if p.staff_set.exists %}
#                 <!-- Перевірка, чи існує працівник для даної позиції та чи існує у нього зображення -->
#                 {% if p.staff_set.first.image %}
#                 <img class="prof-img" src="{{ p.staff_set.first.image.url }}" alt="{{ p.position_staff }}" />
#                 {% else %}
#                 <p>No image available for {{ p.staff_set.first.name }}</p>
#                 {% endif %}
#                 <h6 class="prof-p">{{ p.position_staff }}</h6>
#                 <h5>{{ p.staff_set.first.name }}</h5>
#                 {% else %}
#                 <p>No staff assigned to this position</p>
#                 {% endif %}
#             </div>
#         </div>
#     </div>
#     {% endfor %}



