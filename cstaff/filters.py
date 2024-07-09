import django_filters
from cstaff.models import Staff
from django.contrib.auth.models import User


class StaffFilter(django_filters.FilterSet):
    
    
    class Meta:
        model = User
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }