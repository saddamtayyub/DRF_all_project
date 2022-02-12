from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


class StudentAPI(APIView):
    def get(self, request, id=None, format=None):
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'DATA CREATED SUCCESSFULLY!!'})
        return Response(serializer.errors)

    def put(self, request, format=None):
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'COMPLETE DATA UPDATED SUCCESSFULLY!!'})
        return Response(serializer.errors)

    def patch(self, request, format=None):
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'PARTIAL DATA UPDATED SUCCESSFULLY!!'})
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        id = id
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'Message': 'DATA DELETED SUCCESSFULLY!!'})
