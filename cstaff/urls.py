from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'cstaff'
urlpatterns = [
    path('', views.IndexListView.as_view(), name="index"),
   
    path('profil/<slug:profil_slug>/', views.EmployersProfilDetailView.as_view(), name='employer_profil'),
    path('employers/', views.EmployersListView.as_view(), name='employers_list'),
    
    path('myprofil/', views.MyProfilDetailView.as_view(), name='myprofil'),
    path('myprofil/edit/', views.profile_view, name='edit_myprofil'),
    
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)