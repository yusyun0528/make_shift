from django.contrib import admin
from .models import EmployModel ,ShiftModel

# Register your models here.

admin.site.register(EmployModel)
admin.site.register(ShiftModel)