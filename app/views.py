from django.shortcuts import render
from django.http import HttpResponse
i = 0
# Create your views here.
def say_hello(request):
    return render(request, 'hello.html')

def say_bye(request):
    global i
    i += 1
    return HttpResponse('byeeee = ' + str(i))