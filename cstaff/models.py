from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class Position(models.Model):
    position_staff = models.CharField(max_length=255, verbose_name="Position Title")
    positionID = models.IntegerField(default=5, verbose_name="Position ID")
    
    def __str__(self):
        return self.position_staff

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
        ordering = ['positionID']

class Staff(DirtyFieldsMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", db_index=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Position")
    date_of_employment = models.DateTimeField(auto_now_add=True, verbose_name="Date of Employment")
    salary = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Salary")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True, default=None, verbose_name="Image profil")
    
    email = models.EmailField(max_length=254, verbose_name="Email", unique=True)
    username = models.CharField(max_length=150, verbose_name="Username", unique=True)
    password = models.CharField(max_length=128, verbose_name="Password")

    
    def __str__(self):
        return self.name
    
        
    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"
        ordering = ['name']


    def get_absolute_url(self):
        return reverse('employers', kwargs={'pk': self.pk})



