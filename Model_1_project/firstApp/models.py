from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr=models.CharField(max_length=30)
    email=models.EmailField(max_length=140, default=' ')
    emess = models.CharField(max_length=100, default=' ')

    def __str__(self):
        return self.ename
