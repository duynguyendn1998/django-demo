
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.service.user.forms import RegistrationForm
from blog.models import Posts
from django.contrib.auth.models import User

def posts_json(request):
    qs = Posts.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')

def display_variables(request):
    # define dict example to display variables
    posts = {
        "title": "This is post", 
        "author": "Tuong Duy",
        "content_post": "Have a nice day!"
    }
   
    return render(request, "display_variables.html", posts)

def load_images(request):
    return render(request, "load_image.html")

def blogs_list(request):
   data = {'Posts': Posts.objects.all().order_by('-created_dt')}
   return render(request, 'post/post_list.html', data)

def blog_detail(request, id):
   post =  Posts.objects.get(id = id)
   data = {'post': post,
            'user': User.objects.get(id = post.user_id)
   }
   return render(request, 'post/post_detail.html', data)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/')
    return render(request, 'user/register.html', {'form': form})

def dummy_data(request):
    try:
        user = User.objects.get(user_name= 'abc')
    except User.DoesNotExist:
        user = User(user_name= 'abc', email='abc@tma.com.vn', password='12345678x@X')
        user.save()

    user = User.objects.get(user_name= 'abc')
    return HttpResponse(user)
