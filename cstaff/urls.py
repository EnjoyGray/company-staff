from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


app_name = 'cstaff'
urlpatterns = [
    # path('', views.index, name="index")
    path('', views.StaffListView.as_view(), name="index"),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)