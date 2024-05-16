from django.db import models

# Create your models here.

class Position(models.Model):
    position_staff = models.CharField(max_length=255)
    pisitionID = models.IntegerField(default=5, verbose_name="ID - position")
    
    def __str__(self):
        return self.position_staff
    
    
class Staff(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Position in work")
    date_of_employment = models.DateTimeField(auto_now_add=True, verbose_name="Date of employment")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salary worker")
    
    def __str__(self):
        return self.name


