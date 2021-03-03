from django.contrib import admin
from django.urls import path
from .views import signup_func ,login_func ,list_func ,logout_func ,update_func ,EmployCreate ,delete_func, make_shift_func 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_func ,name='signup'),
    path('login/', login_func ,name='login'),
    path('list/', list_func ,name='list'),
    path('logout/', logout_func ,name='logout'),
    path('create/', EmployCreate.as_view(), name='create'),
    path('update/<int:pk>',update_func ,name ='update'),    
    path('delete/<int:pk>',delete_func , name='delete'),
    path('make_shift/',make_shift_func ,name='make_shift')
]
