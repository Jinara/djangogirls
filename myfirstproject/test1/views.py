from django.http import HttpResponse
from django.shortcuts import render

def myfirstview(request, param):
  return HttpResponse("Holii this is my first app with DJango, my name is %s" % param)
