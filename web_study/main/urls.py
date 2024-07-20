from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    
    # 수정
    path('blog/<int:post_id>/', views.posting, name="posting"),
    
    path('blog/new_post/', views.new_post, name='new_post'),
    ]