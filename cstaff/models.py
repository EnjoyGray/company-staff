from django.db import models
from django.urls import reverse

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

class Staff(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", db_index=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Position")
    date_of_employment = models.DateTimeField(auto_now_add=True, verbose_name="Date of Employment")
    salary = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Salary")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True, default=None, verbose_name="Image profil")
    
    
    def __str__(self):
        return self.name
    
    
    
    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"
        ordering = ['name']


    def get_absolute_url(self):
        return reverse('employers', kwargs={'pk': self.pk})

