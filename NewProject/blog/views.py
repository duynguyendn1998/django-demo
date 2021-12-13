
from django.core import serializers
from django.http import HttpResponse, response

from blog.models import Posts

def some_view(request):
    qs = Posts.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')
