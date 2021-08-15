from json.decoder import JSONDecodeError
from django.db import models
from django.contrib.auth.models import User
import json

from django.db.models import base
from django.http.response import JsonResponse

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Title", null=False, blank=False)
    content = models.TextField(verbose_name="Content", null=False, blank=False)
    created_in = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name="Created")
    likes = models.TextField(blank=True, null=True)
    views = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to="posts", verbose_name="Photo")

    def __str__(self):
        return f"{self.title}"

    def count_views(self):
        try:
            view_list = json.loads(self.views)
            return len(view_list['views'])
        except JSONDecodeError:
            return 0

    def count_likes(self):
        try:
            likes_list = json.loads(self.likes)
            return len(likes_list['likes'])
        except JSONDecodeError:
            return 0