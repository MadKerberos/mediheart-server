from django.db import models

# Create your models here.
class BloodType(models.Model):
    class Meta:
        app_label = "api"
        db_table = 'api_bloodtype'

    BLOODTYPE_CHOICES = (
        ('A+', 'A+ Blood Type'),
        ('A-', 'A- Blood Type'),
        ('B+', 'B+ Blood Type'),
        ('B-', 'B- Blood Type'),
        ('AB+', 'AB+ Blood Type'),
        ('AB-', 'AB- Blood Type'),
        ('0+', '0+ Blood Type'),
        ('0-', '0- Blood Type'),
    )

    label = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES)
    
    def __str__(self):
       return str(str(self.__dict__))