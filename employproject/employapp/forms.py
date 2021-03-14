from django.forms import ModelForm
from .models import EmployModel ,ShiftModel

class EmployForm(ModelForm):
    class Meta:
        model = EmployModel
        fields = ( 'worker_name','work_day0','work_day1','work_day2','work_day3','work_day4','work_day5','work_day6',
                    'work_day7', 'work_day8','work_day9','work_day10','work_day11','work_day12','work_day13','work_day14','work_day15',
                    'work_day16','work_day17','work_day18','work_day19','manager','employer')

class ShiftForm(ModelForm):
    class Meta:
       model = ShiftModel
       fields = ('need_people','times','manager','employer')
        