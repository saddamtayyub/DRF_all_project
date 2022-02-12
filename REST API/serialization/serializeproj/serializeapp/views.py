from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Employees
from .serializers import EmpSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse

# Create your views here.

# model object(one row) asking for id then sending result to user
def emp_details_serialized(request, id):
    emp = Employees.objects.get(id=id)
    # print(emp)
    serialized_dt = EmpSerializer(emp)
    # print(serialized_dt)
    # print(serialized_dt.data)
    # json_data = JSONRenderer().render(serialized_dt.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serialized_dt.data)

# Query set(whole table of employees)
def emp_list_details_serialized(request):
    emp = Employees.objects.all()
    # print(emp)
    serialized_dt = EmpSerializer(emp, many=True)
    # print(serialized_dt)
    # print(serialized_dt.data)
    # json_data = JSONRenderer().render(serialized_dt.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serialized_dt.data, safe=False)
