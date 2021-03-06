from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create Posts models.
class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default="") # update to foreign key --> it is user_id in Posts table of database
    title = models.CharField(max_length=100)
    content_post = models.TextField() # data type text
    created_dt = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category')

    def __str__(self): # display title instead of object
        return self.title

# Create Comments models.
class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default="")  # update to foreign key --> it is user_id in Comments table of database
    post = models.ForeignKey(Posts,on_delete=models.CASCADE, default="")  # update to foreign key --> it is post_id in Comments table of database
    content_comment = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)

    @admin.display(ordering='user___user_name')
    def user_name(self):
        return self.user.user_name
        
# Create Category models.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name