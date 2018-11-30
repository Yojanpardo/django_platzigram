#Django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#utilities
from datetime import datetime

def hello_world(request):
	return HttpResponse('Hello world!\nCurrent time server is: {now}'.format(
		now=datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs')
	))

def ordering(request):
	numbers = request.GET['numbers']
	numbers = list(numbers.split(','))
	parsed_numbers = list()
	
	for number in numbers:
		number = int(number)
		parsed_numbers.append(number)

	ordered_numbers = sorted(parsed_numbers)
	#import pdb; pdb.set_trace() #esta linea permite hacer un debug delicioso
	return JsonResponse({'Numbers':ordered_numbers})

def access(request,name,age):
	if age < 12:
		message = '{}, no tienes la edad suficiente para poder acceder a platzigram'.format(name)
	else:
		message = 'Bienvenido a platzigram, {}'.format(name)

	return HttpResponse(message)

def home(request):
	return render(request,'home.html')