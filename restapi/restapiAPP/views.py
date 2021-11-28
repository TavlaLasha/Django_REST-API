from decimal import Context
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls.resolvers import URLPattern, URLResolver
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer

from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.response import Response
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

# @api_view(['GET'])
# @renderer_classes((XMLRenderer,))
@csrf_exempt
def get_all_persons(request):
    #JSON Version

    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many = True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)

    #XML Version

    # if request.method == 'GET':
    #     persons = Person.objects.all()
    #     serializer = PersonSerializer(persons, many = True)
    #     return Response(serializer.data)

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

# @api_view(['POST'])
# @parser_classes((XMLParser,))
@csrf_exempt
def add_person(request):
    #JSON Version

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'ErrorMessage: ' : 'Bad Request'}, status=400)

    #XML Version

    # if request.method == 'POST':
    #     data = XMLParser().parse(request)
    #     serializer = PersonSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

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

def get_urls(request):
    info=[]
    for p in list_urls(urls.urlpatterns):
        info.append(p[0])

    context ={
        'data' : info
    }
    
    return render(request, 'index.html', context)

import restapiAPP.urls as urls


def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    yield from list_urls(lis[1:], acc)