from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import fields
from blog.models import Posts
from blog.service.post.post_form import PostCreateForm
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
    form_class = PostCreateForm
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return HttpResponseRedirect('/blog/')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

class PostUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'content_post']
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/blog/')