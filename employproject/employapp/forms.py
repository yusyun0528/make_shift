from django.forms import ModelForm
from .models import EmployModel

class EmployForm(ModelForm):
    class Meta:
        model = EmployModel
        fields = ( 'worker_name','work_day0','work_day1','work_day2','work_day3','work_day4','work_day5','work_day6',
                'work_day7', 'work_day8','work_day9','manager','employer')