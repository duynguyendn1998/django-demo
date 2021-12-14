from rest_framework import serializers

from blog.models  import Posts

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ['id', 'title', 'content_post', 'created_dt']