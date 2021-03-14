from django.contrib import admin
from django.urls import path
from .views import home_func ,signup_func ,login_func ,setting_require ,SettingCreate ,list_func ,logout_func ,update_func ,setting_update ,create_func ,delete_func, make_shift_func 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_func ,name='home'),
    path('signup/', signup_func ,name='signup'),
    path('login/', login_func ,name='login'),
    path('setting-require', setting_require ,name='require'),
    path('setting/',SettingCreate.as_view() ,name='setting'),
    path('list/', list_func ,name='list'),
    path('logout/', logout_func ,name='logout'),
    path('create/', create_func, name='create'),
    path('update/<int:pk>',update_func ,name ='update'),
    path('setting_update/<int:pk>',setting_update, name='setting_update'),    
    path('delete/<int:pk>',delete_func , name='delete'),
    path('make_shift/',make_shift_func ,name='make_shift')
]
