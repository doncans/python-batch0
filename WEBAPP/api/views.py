from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import EmployeeSerializer
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
@api_view(['POST','GET'])
def index(request):
    if request.method == 'GET':
        context = {"Message":"WelCome To Get Method"}
        return Response(context)
    if request.method == 'POST':
        data = request.data
        context = {"Message":data}
        return Response(context)
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def serializer_view(request):
    if request.method == 'GET':
        emp_data = Employee.objects.all()
        serializer = EmployeeSerializer(emp_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "PUT":
        print("Update resource")
    elif request.method == "DELETE":
        print("Delete resource")
    else:
        print("Error")