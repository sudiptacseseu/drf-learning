from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # Setting single field attribute
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # fields = '__all__'

        # Setting multiple field attribute
        # read_only_fields = ['name', 'roll']

        # Another method to apply attribute
        # extra_kwargs = {'name': {'read_only': True}}
