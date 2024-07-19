from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, F
from django.http import HttpResponse, JsonResponse
from .models import Staff, Position, StaffGroup
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import LoginUserForm, StaffForm, UserForm, UserRegistrationForm, ProfileUserForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from django.urls import reverse, reverse_lazy
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.http import JsonResponse
from .encoders import DateTimeEncoder
from .filters import StaffFilter



# Create your views here.

class IndexListView(ListView):
    model = Staff
    template_name = "cstaff/index.html"
    context_object_name = 'positions'
    title_page = 'Home'

    def get_queryset(self):
        return Position.objects.filter(pk__in=[1, 2, 3, 4])


def employers_view(request):
    data = {
        "name": "John Doe",
        "hired_at": datetime.now()
    }
    
    return JsonResponse(data, encoder=DateTimeEncoder)

    
 
class EmployersListView(ListView):
    model = User
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
        context['filter'] = StaffFilter(self.request.GET, queryset=self.get_queryset())

        users_with_profiles = User.objects.select_related('profile').annotate(
            profile_position_staff=F('profile__position__position_staff'),
            profile_date_of_employment=F('profile__date_of_employment'),
            profile_salary=F('profile__salary'),
            profile_image=F('profile__image'),
        ).values('id', 'first_name', 'last_name', 'is_superuser', 'username',
                 'profile_position_staff', 'profile_date_of_employment',
                 'profile_salary', 'profile_image')

        users_list = list(users_with_profiles)
        for user in users_list:
            try:
                staff_member = Staff.objects.get(user_id=user['id'])
                user['profile_absolute_url'] = staff_member.get_absolute_url()
            except Staff.DoesNotExist:
                user['profile_absolute_url'] = "#"

        context['qs_json'] = json.dumps(users_list, cls=DjangoJSONEncoder)
        return context

                
   
class EmployersProfilDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "cstaff/employers_profil.html"
    slug_url_kwarg = "profil_slug"
    context_object_name = 'profil'
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profil'] = self.get_object().profile
        context['user'] = self.get_object()
            
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(User, 
                                 username=self.kwargs[self.slug_url_kwarg])
    
    
   

# -------------users--------------------

        
class MyProfilDetailView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "cstaff/myprofil.html"
    extra_context = {
        'title': "My Profil",
    }

    def get_success_url(self):
        return reverse_lazy('cstaff:index')

    def get_object(self, queryset=None):
        return self.request.user



@login_required
def profile_view(request):
    user = request.user
    try:
        staff = user.profile  # отримуємо пов'язану модель Staff через OneToOne
    except Staff.DoesNotExist:
        staff = Staff(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        staff_form = StaffForm(request.POST, request.FILES, instance=staff)
        if user_form.is_valid() and staff_form.is_valid():
            user_form.save()
            staff_form.save()
            return redirect('cstaff:myprofil')  # замініть 'profile' на ваше посилання
    else:
        user_form = UserForm(instance=user)
        staff_form = StaffForm(instance=staff)

    context = {
        'user_form': user_form,
        'staff_form': staff_form,
    }
    return render(request, 'cstaff/myprofil_edit.html', context)


class EditMyProfilDetailView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "cstaff/myprofil_edit.html"
    extra_context = {
        'title': "My Profil",
    }

    def get_success_url(self):
        return reverse_lazy('cstaff:myprofil')

    def get_object(self, queryset=None):
        return self.request.user



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
