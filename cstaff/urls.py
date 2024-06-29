from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'cstaff'
urlpatterns = [
    path('', views.IndexListView.as_view(), name="index"),
    path('employers/', views.EmployersListView.as_view(), name="employers"),
    path('myprofil/', views.MyProfilDetailView.as_view(), name='myprofil'),
    path('myprofil/edit/', views.EditMyProfilDetailView.as_view(), name='edit_myprofil'),
    path('profil_employers/<int:pk>/', views.EmployersProfilDetailView.as_view(), name='employers_profil'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)