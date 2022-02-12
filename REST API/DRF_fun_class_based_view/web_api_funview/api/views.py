from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, id=None):
    if request.method == "GET":
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'DATA CREATED SUCCESSFULLY!!'})
        return Response(serializer.errors)

    if request.method == "PUT":
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'COMPLETE DATA UPDATED SUCCESSFULLY!!'})
        return Response(serializer.errors)

    if request.method == "PATCH":
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'PARTIAL DATA UPDATED SUCCESSFULLY!!'})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = id
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'Message': 'DATA DELETED SUCCESSFULLY!!'})
