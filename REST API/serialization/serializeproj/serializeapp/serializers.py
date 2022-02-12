from rest_framework import serializers


class EmpSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    emp_id = serializers.IntegerField()
    city = serializers.CharField(max_length=200)
