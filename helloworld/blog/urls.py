from django.urls import path
from django.urls.base import reverse
from blog import views
from django.contrib.auth import views as auth_views #Because use User default of django --> rename views to auth_view avoid confusion 
from blog.service.post.post_service import PostDeleteView, PostListViewJson, PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
   path('post_serializers', views.posts_json),
   path('post_json',PostListViewJson.as_view()),
   path('display_variables', views.display_variables),
   path('load_images',views.load_images),
   # path('',views.blogs_list),
   # path('<int:id>', views.blog_detail, name='post detail'),
   path('register/', views.register, name="register"),
   path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
   path('logout/', auth_views.LogoutView.as_view(next_page='/blog/'),name='logout'),
   path('', PostListView.as_view(), name='blog'),
   path('<int:pk>', PostDetailView.as_view(), name='detail_post'),
   path('new_post/', PostCreateView.as_view(), name='create_post'),
   path('<int:pk>/update', PostUpdateView.as_view()),
   path('<int:pk>/delete', PostDeleteView.as_view()),
]