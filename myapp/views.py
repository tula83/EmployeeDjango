from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Employee
from django.core import serializers

# Create your views here.


data = [

    {"id": 1, "name": "tularaemia", "address": "babai-7 Nepal"},
    {"id": 2, "name": "tularam", "address": "babai-7 Nepal"},
    {"id": 3, "name": "tularam", "address": "babai-7 Nepal"},
]


def get_data(request, name=None):
    if request.method == 'GET':
        if name is not None:
            employee_object = Employee.objects.get(name=name)
            if employee_object:
                employee_dict = employee_object.to_dict()
                return JsonResponse(employee_dict, safe=False, status=200)
            else:
                return JsonResponse({"message": "not found"}, status=404)
        else:
            employee = (Employee.objects.all().values())
            return JsonResponse(list(employee), safe=False)

    if request.method == 'POST':
        print('tula')


def emp_info(request):
    if request.method == 'GET':
        return JsonResponse(data, safe=False)


@csrf_exempt
def get_employee(request):
    if request.method == 'POST':
        try:
            get_data = request.body
            print(f'Received JSON data: {get_data}')

            data_str = get_data.decode('utf-8').strip()
            data_dict = json.loads(data_str)
            name = data_dict.get("name")
            email = data_dict.get("email")

            emp = Employee(name=name, email=email)
            emp.save()
            return JsonResponse({'message': "created successfully"}, status=201)

        except Exception as e:
            return JsonResponse({"error": "invalid json-data"}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# class based view
class EmployeeCreateView(View):

    def post(self, request, *args, **kwargs):
        try:
            # Get JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            name = data.get("name")
            email = data.get("email")

            # Validate and save the data
            if name and email:
                emp = Employee(name=name, email=email)
                emp.save()
                return JsonResponse({'message': "Employee created successfully"}, status=201)
            else:
                return JsonResponse({"error": "Invalid data. Both 'name' and 'email' are required."}, status=400)
        except Exception as e:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
