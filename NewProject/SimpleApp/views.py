from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def home(request):
    response = HttpResponse()
    response.writelines ('<h2> Hello World </h2>')
    response.write ('This is Simple App')
    return response

