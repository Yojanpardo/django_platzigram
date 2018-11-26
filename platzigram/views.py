#Django
from django.http import HttpResponse, JsonResponse

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
	import pdb; pdb.set_trace()
	return HttpResponse(str(ordered_numbers))