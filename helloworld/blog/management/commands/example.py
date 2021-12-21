from typing import List
from django.db import connection, reset_queries
from django.core.management.base import BaseCommand
from blog.models import Posts
from django.core import serializers

import time
import functools

def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print("Function : " + func.__name__)
        print("Number of Queries : {}".format(end_queries - start_queries))
        print("Finished in : {}".format(end - start))

        return result

    return inner_func

class Command(BaseCommand):

    @query_debugger
    def posts_user_list(self):
        queryset = Posts.objects.filter(title__icontains='hello').select_related('user')
        posts = []
        for post in queryset:
            posts.append({"name": post.title, "author": post.user.user_name})
        print (posts)

    @query_debugger
    def posts_category_list(self):
        queryset = Posts.objects.prefetch_related('categories')
        posts = []
        for post in queryset:
            posts.append({"name": post.title, "category": post.categories.name})
        print (posts)

    def parse_response_json(self):
        qs = Posts.objects.filter(title__icontains='heLlo') # get row have title contains 'hello'
        # get full queryset
        # qs_json = serializers.serialize('json', qs)
        # only get field 'title','content_post' of fields
        qs_json = serializers.serialize('json', qs, fields=('title','content_post'))
        print (qs_json)

    def handle(self, *args, **options):
        self.parse_response_json()
        # print(self.get_queryset())
        # self.posts_user_list()
        # self.posts_category_list()