from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to My Shop!")

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to My Shop!")

def orders_list(request):
    return HttpResponse("Here is where orders will be displayed.")
def create_order(request):
    return HttpResponse("This page will allow creating a new order.")
from django.http import JsonResponse

def products_list(request):
    data = [
        {"id": 1, "name": "Shoe", "price": 100},
        {"id": 2, "name": "Watch", "price": 200},
        {"id": 3, "name": "Cloth", "price": 150},
    ]
    return JsonResponse(data, safe=False)

def add_to_cart(request):
    return JsonResponse({"message": "Item added to cart!"})
