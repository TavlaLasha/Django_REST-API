from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer

@csrf_exempt
def get_all_persons(request):

    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many = True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)

@csrf_exempt
def get_person(request, pn):

    if request.method == 'GET':
        try:
            person = Person.objects.get(pn=pn)
        except Person.DoesNotExist:
            return JsonResponse({'ErrorMessage: ' : 'Person not found'}, status=404)

        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)

@csrf_exempt
def add_person(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)

@csrf_exempt
def edit_person(request, pn):

    if request.method == 'PUT':
        try:
            person = Person.objects.get(pn=pn)
        except Person.DoesNotExist:
            return JsonResponse({'ErrorMessage: ' : 'Person not found'}, status=404)
            
        data = JSONParser().parse(request)
        serializer = PersonSerializer(person, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)

@csrf_exempt
def delete_person(request, pn):

    if request.method == 'DELETE':
        try:
            person = Person.objects.get(pn=pn)
        except Person.DoesNotExist:
            return JsonResponse({'ErrorMessage: ' : 'Person not found'}, status=404)
            
        person.delete()

        return HttpResponse(status=204)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)