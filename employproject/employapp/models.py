from django.db import models

# Create your models here.
class EmployModel(models.Model):
        worker_name =models.CharField( max_length=100 )
        work_day0 = models.BooleanField(default=False)
        work_day1 = models.BooleanField(default=False)
        work_day2 = models.BooleanField(default=False)
        work_day3 = models.BooleanField(default=False)
        work_day4 = models.BooleanField(default=False)
        work_day5 = models.BooleanField(default=False)
        work_day6 = models.BooleanField(default=False)
        work_day7 = models.BooleanField(default=False)
        work_day8 = models.BooleanField(default=False)
        work_day9 = models.BooleanField(default=False)
        manager = models.BooleanField(default=False)    
        employer =models.CharField(max_length=100 ,default='')

class ShiftModel(models.Model):
    upload_dir = models.FileField(upload_to='file/%Y/%m/%d')
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.upload_diername)
     