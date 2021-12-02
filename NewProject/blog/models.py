from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)

class Posts(models.Model):
    user_id: models.IntegerField()
    title = models.CharField(max_length=100)
    content_post = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    user_id: models.IntegerField()
    post_id: models.IntegerField()
    content_comment = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
