from api.models.bloodtype import BloodType
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Patients(models.Model):
    class Meta:
        app_label = "api"
        db_table = 'api_patients'

    # Choises Values
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    firstname = models.CharField(max_length = 50,null=True)
    lastname = models.CharField(max_length = 50,null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    bloodType = models.ForeignKey(BloodType, on_delete=models.CASCADE,null=True)
    fk_user = models.ForeignKey(User, on_delete = models.CASCADE,null=True, unique=True)
    
    def __str__(self):
       return str(str(self.__dict__))