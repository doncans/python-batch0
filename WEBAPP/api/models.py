from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_sal = models.CharField(max_length=200)
    emp_design = models.CharField(max_length=200)

    def __str__(self):
        return self.emp_name