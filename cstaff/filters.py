import django_filters
from django.contrib.auth.models import User
from cstaff.models import Staff


class StaffFilter(django_filters.FilterSet):
    profile__salary = django_filters.RangeFilter()
    
    class Meta:
        model = User
        fields = {
            'profile__position': ['lte', 'gte',],
            'profile__group': ['exact'],
            'profile__group_leader': ['exact'],
        }
        
