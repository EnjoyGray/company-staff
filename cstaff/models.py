from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Position(models.Model):
    position_staff = models.CharField(
        max_length=255,
        verbose_name="Position Title"
    )
    
    def __str__(self):
        return self.position_staff

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
        ordering = ['id']


class StaffGroup(models.Model):
    group_staff = models.IntegerField(verbose_name="Group")
    
    def __str__(self):
        return str(self.group_staff) 

    class Meta:
        verbose_name = "Staff Group" 
        verbose_name_plural = "Staff Groups"
        ordering = ['id']


def get_default_position():
    return Position.objects.get(id=5)

def get_default_group():
    return StaffGroup.objects.get(id=1)



class StaffGroup(models.Model):
    group_staff = models.IntegerField(verbose_name="Group")
    
    def __str__(self):
        return str(self.group_staff) 

    class Meta:
        verbose_name = "Staff Group" 
        verbose_name_plural = "Staff Groups"
        ordering = ['id']
        

def get_default_position():
    return Position.objects.get(id=5)

def get_default_group():
    return StaffGroup.objects.get(id=1)


class Staff(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        blank=True,
        default=get_default_position,
        verbose_name="Position"
    )
    group = models.ForeignKey(
        StaffGroup,
        on_delete=models.CASCADE,
        blank=True,
        default=get_default_group,
        verbose_name="Group Staff"
    )
    
    group_leader = models.IntegerField(
        blank=True,
        default=None,
        null=True,
        verbose_name="Leader Group"
        )
    
    
    date_of_employment = models.DateTimeField(auto_now_add=True, verbose_name="Date of Employment")
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Salary")
    image = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Image profil"
    )
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"
        ordering = ['user']

    def get_absolute_url(self):
        return reverse('employers', kwargs={'pk': self.pk})
