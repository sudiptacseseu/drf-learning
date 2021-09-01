from rest_framework import serializers
from .models import Student


# Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start with R!')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full!')
        return value

    # Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'pritimoy' and city.lower() != 'faridpur':
            raise serializers.ValidationError('City must be Faridpur!')
        return data
