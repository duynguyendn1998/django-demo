from django.urls import path
from blog import views

urlpatterns = [
   path('post_serializers', views.posts_json),
   path('post_json', views.ListPostView.as_view()),
   path('display_variables', views.display_variables)
]