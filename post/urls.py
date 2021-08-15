from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/expand", views.expand_post, name="expand_post"),
    path("<int:post_id>/like_post", views.like_post),
    path("<int:post_id>/undo_ike_post", views.undo_ike_post),
    path('all_posts', views.all_posts, name="all_posts")
]