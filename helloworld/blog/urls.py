from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from blog.post.post_service import ListPostView


urlpatterns = [
   path('post_serializers', views.posts_json),
   path('post_json',ListPostView.as_view()),
   path('display_variables', views.display_variables),
   path('load_images',views.load_images),
   path('',views.blogs_list),
   path('<int:id>', views.blog_detail, name='post detail'),
   path('dummy_data', views.dummy_data),
   path('register/', views.register, name="register"),
   path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
   path('logout/', auth_views.LogoutView.as_view(next_page='/blog/'),name='logout')
]