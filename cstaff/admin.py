from django.contrib import admin
from .models import Position, StaffGroup, Staff

# Register your models here.

# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     fields = ['id', 'image', 'name', 'position', 'salary', 'date_of_employment']
#     readonly_fields = ['id', 'date_of_employment']
#     list_display = ('name', 'id', 'position', 'salary', 'date_of_employment')
#     list_per_page = 30
    
#     search_fields = ['name', 'position__position_staff']  
#     list_filter = ['position']


# @admin.register(Position)
# class PositionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'position_staff', 'positionID')
#     list_display_links = ('id', 'position_staff', 'positionID')
#     ordering = ['positionID']




@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'position_staff']
    search_fields = ['position_staff']
    # Інші налаштування адміністративного інтерфейсу

@admin.register(StaffGroup)
class StaffGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_staff']
    search_fields = ['group_staff']
    # Інші налаштування адміністративного інтерфейсу

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    # fields = ['id', 'image', 'user__username', 'position', 'salary', 'date_of_employment']
    list_display = ['user', 'position', 'group', 'date_of_employment']
    search_fields = ['user__username', 'position__position_staff', 'group__group_staff']
    # Інші налаштування адміністративного інтерфейсу