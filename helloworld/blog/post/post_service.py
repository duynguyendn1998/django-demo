from blog.models import Posts
from blog.post.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView

class ListPostView(ListCreateAPIView):
    model = Posts
    serializer_class = PostSerializer

    def get_queryset(self):
        return Posts.objects.all()