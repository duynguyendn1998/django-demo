from django.views.generic.edit import CreateView
from rest_framework import fields
from blog.models import Posts
from blog.service.post.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from django.views.generic import ListView, DetailView

class PostListViewJson(ListCreateAPIView):
    model = Posts
    serializer_class = PostSerializer

    def get_queryset(self):
        return Posts.objects.all()

class PostListView(ListView):
    queryset = Posts.objects.all().order_by('-created_dt')
    template_name = 'post/post_list.html'
    context_object_name = 'Posts'
    paginate_by = 12

class PostDetailView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'post/post_detail.html'

class PostCreateView(CreateView):
    model = Posts
    fields = ['title', 'content_post']
    template_name = 'post/post_form.html'