from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('create_post', views.create_post, name="create_post"),
    path('<int:post_id>/edit_post', views.edit_post, name="edit_post"),
    path('<int:post_id>/delete_post', views.delete_post, name="delete_post")
]