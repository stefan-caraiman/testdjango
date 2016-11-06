import random

from django.http import HttpResponse


def hello_world(request):
	return HttpResponse("<h1>Hello world.</h1>")

def root_page(request):
	return HttpResponse("<h1>Hello from root page.</h1>")

def random_numer(request, max_rand=100):
	random_number = random.randrange(0, int(max_rand))
	msg = "Random number between 0 and %s : %d" % (max_rand, random_number)
	return HttpResponse(msg)