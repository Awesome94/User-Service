from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse("you have registered successfully")

def login(request):
    return HttpResponse("you have successfull loged in")

def logout(request):
    return HttpResponse("you have suucessfully logged out")
