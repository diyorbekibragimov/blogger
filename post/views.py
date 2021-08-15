from json.decoder import JSONDecodeError
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post

import json

# Create your views here.
def index(request):
    page_title = "Home Page"
    posts = Post.objects.all()[::-1][:3]

    return render(request, 'post/index.html', {
        "posts": posts,
        "page_title": page_title,
    })

def expand_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    page_title = post.title
    liked = False

    # For views
    try:
        dict_name = json.loads(post.views)
    except JSONDecodeError:
        dict_name = {'views': []}

    if request.user.id not in dict_name['views']:
        dict_name['views'].append(request.user.id)
        post.views = json.dumps(dict_name)
        post.save()

    try:
        dict_name = json.loads(post.likes)

        if request.user.id in dict_name['likes']:
            liked = True
    except JSONDecodeError:
        pass

    return render(request, 'post/post.html', {
        "post": post,
        "page_title": page_title,
        'liked': liked
    })

def like_post(request, post_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = get_object_or_404(Post, pk=post_id)
            try:
                dict_name = json.loads(post.likes)
            except JSONDecodeError:
                dict_name = {'likes': []}

            if request.user.id not in dict_name['likes']:
                dict_name['likes'].append(request.user.id)
                post.likes = json.dumps(dict_name)
                post.save()
            return JsonResponse({'liked': True})
    else:
        return redirect('/authentication/login')

def undo_ike_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        try:
            dict_name = json.loads(post.likes)

            if request.user.id in dict_name['likes']:
                dict_name['likes'].remove(request.user.id)

            return JsonResponse({'liked': False})
        except JSONDecodeError:
            pass
    else:
        return redirect('/authentication/login')

def all_posts(request):
    page_title = "All posts"
    posts = Post.objects.all()

    return render(request, 'post/all_posts.html', {
        'posts': posts,
        'page_title': page_title
    })