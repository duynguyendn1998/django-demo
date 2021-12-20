from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = HttpResponse()
    response.writelines ('<h2> Hello World </h2>')
    response.write ('This is Simple App')
    return response

