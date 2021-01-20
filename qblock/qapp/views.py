from django.shortcuts import render
from django.http import JsonResponse

def api_overview():
    return JsonResponse('API BASE POINT', safe=false)
