from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=255)
    phone=models.IntegerField()
    mailid=models.CharField(max_length=255)
    address=models.TextField(max_length=255)
    department=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    purpose=models.CharField(max_length=255)
    meterialprovide=models.CharField(max_length=255)
    def __str__(self):
        return self.name
