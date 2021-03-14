from django.db import models

# Create your models here.
class EmployModel(models.Model):
        worker_name =models.CharField( max_length=100 )
        work_day0 = models.BooleanField(default=False ,blank=True)
        work_day1 = models.BooleanField(default=False ,blank=True)
        work_day2 = models.BooleanField(default=False ,blank=True)
        work_day3 = models.BooleanField(default=False ,blank=True)
        work_day4 = models.BooleanField(default=False ,blank=True)
        work_day5 = models.BooleanField(default=False ,blank=True)
        work_day6 = models.BooleanField(default=False ,blank=True)
        work_day7 = models.BooleanField(default=False ,blank=True)
        work_day8 = models.BooleanField(default=False ,blank=True)
        work_day9 = models.BooleanField(default=False ,blank=True)
        work_day10 = models.BooleanField(default=False ,blank=True)
        work_day11 = models.BooleanField(default=False ,blank=True)
        work_day12 = models.BooleanField(default=False ,blank=True)
        work_day13 = models.BooleanField(default=False ,blank=True)
        work_day14 = models.BooleanField(default=False ,blank=True)
        work_day15 = models.BooleanField(default=False ,blank=True)
        work_day16 = models.BooleanField(default=False ,blank=True)
        work_day17 = models.BooleanField(default=False ,blank=True)
        work_day18 = models.BooleanField(default=False ,blank=True)
        work_day19 = models.BooleanField(default=False ,blank=True)        
        manager = models.BooleanField(default=True ,blank=True)    
        employer =models.CharField(max_length=100 ,default='')

class ShiftModel(models.Model):
    def make_choice():
        choices_nums =[]
        for i in range(1,21):
            choices_nums.append((i,i))
        return tuple(choices_nums)
        
    need_people = models.IntegerField(choices=make_choice() ,default=1)
    times = models.IntegerField(choices=make_choice() ,default=1)
    manager = models.BooleanField(default=True)
    employer =models.CharField( max_length=100 ,default='' )