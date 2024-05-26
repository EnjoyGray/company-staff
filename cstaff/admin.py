from django.contrib import admin
from .models import Staff, Position

# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    fields = ['id', 'image', 'name', 'position', 'salary', 'date_of_employment']
    readonly_fields = ['id', 'date_of_employment']
    list_display = ('name', 'id', 'position', 'salary', 'date_of_employment')
    list_per_page = 30
    
    search_fields = ['name', 'position__position_staff']  
    list_filter = ['position']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_staff', 'positionID')
    list_display_links = ('id', 'position_staff', 'positionID')
    ordering = ['positionID']
