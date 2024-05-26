from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


app_name = 'cstaff'
urlpatterns = [
    path('', views.IndexListView.as_view(), name="index"),
    path('employers/', views.EmployersListView.as_view(), name="employers"),
    path('mprofil/<int:pk>/', views.MProfilDetailView.as_view(), name='mprofil'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)