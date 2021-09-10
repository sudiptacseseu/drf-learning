from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

# Hyperlinked model serializer gives default field named url
# class StudentSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Student
#         fields = ['id', 'url', 'name', 'roll', 'city']
