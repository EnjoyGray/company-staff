from datetime import datetime
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .models import Staff, Position
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import LoginUserForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm
from cstaff.models import Staff
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


# Create your views here.

class IndexListView(ListView):
    model = Staff
    template_name = "cstaff/index.html"
    context_object_name = 'positions'
    title_page = 'Home'

    def get_queryset(self):
        return Position.objects.filter(pk__in=[1, 2, 3, 4])
    
    
 
class EmployersListView(ListView):
    model = Staff
    template_name = "cstaff/employers.html"
    context_object_name = 'employers'
    title_page = 'Employers'
    paginate_by = 25

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'id')
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']
        context['page_range'] = paginator.get_elided_page_range(page_obj.number)
        context['current_ordering'] = self.get_ordering()
        return context
    
    
class SearchResultsView(ListView):
    model = Staff
    template_name = 'cstaff/search_results.html'
    context_object_name = 'employers'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            if query.isdigit():  # Check if the input is a digit for ID search
                return Staff.objects.filter(id=int(query))
            else:
                return Staff.objects.filter(
                    Q(name__icontains=query) |
                    Q(position__position_staff__icontains=query) |
                    Q(date_of_employment__icontains=query)
                )
        return Staff.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            employers = list(context['employers'].values('id', 'name', 'position__position_staff', 'date_of_employment', 'salary'))
            return JsonResponse({'employers': employers})
        return super().render_to_response(context, **response_kwargs)
        
    
class MProfilDetailView(DetailView):
    model = Staff
    template_name = "cstaff/profil.html"
    context_object_name = 'profil'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
def profiltest(request):
    return render(request, "cstaff/profil.html")

# def index(request):
#     return render(request, "cstaff/index.html")
   

# -------------users--------------------




class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'cstaff/login.html'
    extra_context = {'title': 'Login'}
    
    def get_success_url(self):
        return reverse_lazy('cstaff:index')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Користувача успішно зареєстровано!')
            return redirect('cstaff:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'cstaff/register.html', {'form': form})
