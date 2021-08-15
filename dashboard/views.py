from dashboard.forms import PostForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from post.models import Post

# Create your views here.
def index(request):
    page_title = "Dashboard"
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html', {
            'page_title': page_title,
            'posts': Post.objects.filter(creator=request.user)
        })
    else:
        return redirect('/authentication/login')


def profile(request):
    page_title = "Profile page"
    if request.user.is_authenticated:
        return render(request, 'dashboard/profile.html', {
            'page_title': page_title
        })
    else:
        return redirect('/authentication/login')

def create_post(request):
    page_title = "Create a post"
    form = PostForm()

    if request.user.is_authenticated:
        if request.method == 'POST':
            data = {
                'creator': request.user.id,
                'title': request.POST['title'],
                'content': request.POST['content'],
            }
            form = PostForm(data, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("dashboard:index")
            else:
                return render(request, 'dashboard/post_create.html', {
                    'page_title': page_title,
                    'error': "Please, fill out all fields.",
                    'form': form,
                })
        else:
            return render(request, 'dashboard/post_create.html', {
                'page_title': page_title,
                'form': form
            })
    else:
        return redirect('/authenticate/login')

def edit_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        page_title = "Editing " + post.title
        
        return render(request, 'dashboard/edit_post.html', {
            'page_title': page_title,
            'post': post
        })
    else:
        return redirect('/authentication/login')

def delete_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return redirect(reverse('dashboard:index'))
    else:
        return redirect('/authentication/login')