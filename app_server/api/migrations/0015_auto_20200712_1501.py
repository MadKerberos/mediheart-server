# Generated by Django 3.0.4 on 2020-07-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200712_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodtype',
            name='bloodType',
            field=models.CharField(choices=[('A+', 'A+ Blood Type'), ('A-', 'A- Blood Type'), ('B+', 'B+ Blood Type'), ('B-', 'B- Blood Type'), ('AB+', 'AB+ Blood Type'), ('AB-', 'AB- Blood Type'), ('0+', '0+ Blood Type'), ('0-', '0- Blood Type')], max_length=3),
        ),
    ]
