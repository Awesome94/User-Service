from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse("you have registered successfully")

def login(request):
    return HttpResponse("you have successfull loged in")

def logout(request):
    return HttpResponse("you have suucessfully logged out")

def users(request):
    return HttpResponse("All users are here now ")


what are u not allowed to do?
