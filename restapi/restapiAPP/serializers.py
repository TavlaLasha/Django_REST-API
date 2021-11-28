from django.db.models import fields
from rest_framework import serializers
from .models import Person

# class PersonSerializer(serializers.Serializer):
#     firstname = serializers.CharField(max_length=50)
#     lastname = serializers.CharField(max_length=50)
#     pn = serializers.CharField(max_length=11)
#     birthdate = serializers.DateTimeField()
#     gender = serializers.CharField(max_length=6)
#     email = serializers.EmailField()
#     phone = serializers.CharField(max_length=9)

#     def create(self, validated_data):
#         return Person.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.firstname = validated_data.get('firstname', instance.firstname)
#         instance.lastname = validated_data.get('lastname', instance.lastname)
#         instance.pn = validated_data.get('pn', instance.pn)
#         instance.birthdate = validated_data.get('birthdate', instance.birthdate)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.save()

#         return instance

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'