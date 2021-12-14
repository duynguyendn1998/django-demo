
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from blog.models import Posts
from blog.serializers import PostSerializer

def posts_json(request):
    qs = Posts.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')

class ListPostView(ListCreateAPIView):
    model = Posts
    serializer_class = PostSerializer

    def get_queryset(self):
        return Posts.objects.all()

def display_variables(request):
    # define dict example to display variables
    posts = {
        "title": "This is post", 
        "author": "Tuong Duy",
        "content_post": "Have a nice day!"
    }
   
    return render(request, "display_variables.html", posts)