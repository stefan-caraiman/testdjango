from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("You're in the polls index.")

# Create your views here.
