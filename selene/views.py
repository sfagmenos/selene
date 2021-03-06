from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import create
import time
import random

# Create your views here.
@api_view(['GET'])
def walk(request):
    if request.method == 'GET':
        r = create.Create('/dev/tty.ElementSerial-ElementSe')
        done = r.walk()
        if not done:
            return JsonResponse({'response': 503})
        return JsonResponse({'response': 200})
    return JsonResponse({'response': 404})

@api_view(['GET'])
def turn(request):
    pass

@api_view(['GET'])
def u_turn(request):
    response=JsonResponse({'response': 503})
    if request.method == 'GET':
        r = create.Create('/dev/tty.ElementSerial-ElementSe')
        r.turn(183)
        response = JsonResponse({'response': 200})
    return response

@api_view(['GET'])
def walk_left(request):
    response=JsonResponse({'response': 503})
    if request.method == 'GET':
        r = create.Create('/dev/tty.ElementSerial-ElementSe')
        done = r.walk_left()
        if not done:
            return JsonResponse({'response': 503})
        return JsonResponse({'response': 200})
    return JsonResponse({'response': 404})

@api_view(['GET'])
def walk_right(request):
    response=JsonResponse({'response': 503})
    if request.method == 'GET':
        r = create.Create('/dev/tty.ElementSerial-ElementSe')
        done = r.walk_right()
        if not done:
            return JsonResponse({'response': 503})
        return JsonResponse({'response': 200})
    return JsonResponse({'response': 404})

@api_view(['GET'])
def walk_back(request):
    response=JsonResponse({'response': 503})
    if request.method == 'GET':
        r = create.Create('/dev/tty.ElementSerial-ElementSe')
        done = r.walk_right()
        if not done:
            return JsonResponse({'response': 503})
        return JsonResponse({'response': 200})
    return JsonResponse({'response': 404})

@api_view(['GET'])
def wwalk(request):
    if request.method == 'GET':
        distance=1
        r = create.Create('/dev/tty.ElementSerial-ElementSe')
        if (r.walk()):
            return JsonResponse({'response': 200})
    return JsonResponse({'response': 503})
