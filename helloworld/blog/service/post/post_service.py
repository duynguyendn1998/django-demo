from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.models import Posts
from blog.service.post.post_form import PostCreateForm, PostUpdateForm
from blog.service.post.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from django.views.generic import ListView, DetailView

class PostListViewJson(ListCreateAPIView):
    model = Posts
    serializer_class = PostSerializer

    def get_queryset(self):
        return Posts.objects.all()

class PostListView(ListView):
    queryset = Posts.objects.all().order_by('-created_dt') # get all posts and sorted by date 
    template_name = 'post/post_list.html' # define template display
    context_object_name = 'Posts' # name of variable to access from templates (default: object)
    paginate_by = 12 #the number of items (post) displayed on UI

class PostDetailView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'post/post_detail.html'

class PostCreateView(CreateView): # class create class
    form_class = PostCreateForm # class form of post from PostCreateForm
    template_name = 'post/post_form.html' # template display in UI

    def form_valid(self, form): # implementation for form_valid() simply redirects to the success_url.
        post = form.save(commit=False)  # create a model instance return an object that hasn't yet been saved to the database.
        post.user = self.request.user # get user from request to save in db with many to one relationship with model
        post.save() # save model to database
        form.save_m2m() # save checkbox in form to table have many to many relationship
        return HttpResponseRedirect('/blog/') # if success redirect to list blog

    def get_form_kwargs(self, *args, **kwargs): #Build the keyword arguments required to instantiate the form.
        kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['request'] = self.request.user # add current user to 
        return kwargs

class PostUpdateView(UpdateView):
    model = Posts
    form_class = PostUpdateForm
    template_name = 'post/post_form.html'
    success_url ="/blog/" # redirect to blog_list when action success 

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'post/posts_confirm_delete.html'
    success_url ="/blog/"