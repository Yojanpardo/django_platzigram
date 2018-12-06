from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'

class PostsView(LoginRequiredMixin,ListView):
    template_name = 'posts/posts.html'
    model = Post
    ordering = '-created'
    #paginate_by = 2
    context_object_name = 'posts'


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name = 'posts/create_post.html',
        context = {
            'form':form,
            'user':request.user,
            'profile':request.user.profile
        }
    )