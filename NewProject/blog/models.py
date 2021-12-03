from django.db import models
from django.db.models.fields.reverse_related import ManyToOneRel

# Create Users models.
class Users(models.Model):
    user_name = models.CharField(max_length=50) # data type varchar with max_length 100
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    created_dt = models.DateTimeField(auto_now_add=True) # data type timestamptz and auto add when insert row

# Create Posts models.
class Posts(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE, default="") # update to foreign key --> it is user_id in Posts table of database
    title = models.CharField(max_length=100)
    content_post = models.TextField() # data type text
    created_dt = models.DateTimeField(auto_now_add=True) 

# Create Comments models.
class Comments(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE, default="")  # update to foreign key --> it is user_id in Comments table of database
    post = models.ForeignKey(Posts,on_delete=models.CASCADE, default="")  # update to foreign key --> it is post_id in Comments table of database
    content_comment = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)