from django.conf.urls import url, include
from . import views

# This is app_one
urlpatterns = [
# root route to index method
    url(r'^$', views.index, name='index'),
    url(r'^all_likes/(?P<post_id>\d+)$', views.all_likes, name='all_likes'),
    url(r'^users/(?P<user_id>\d+)$', views.users, name='users'),
    url(r'^create_idea$', views.create_idea, name='create_idea'),
    url(r'^like_idea/(?P<post_id>\d+)$', views.like_idea, name='like_idea'),
    url(r'^delete_post/(?P<post_id>\d+)$', views.delete_post, name='delete_post'),
]
