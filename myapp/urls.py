from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import EmployeeCreateView

# from current folder import  views
urlpatterns = [
    path('getData/<str:name>', views.get_data, name='get_data'),
    path('getData/', views.get_data, name='get_data'),

    path('api/getEmployee/', views.get_employee, name='get_employee'),
    path('empInfo/', views.emp_info, name='emp_info'),
    path('insert/',csrf_exempt(EmployeeCreateView.as_view()),name='createEmployee')

]
