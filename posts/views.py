from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostForm

from .models import Post

# Create your views here.

@login_required
def posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request,'posts/posts.html',{'posts':posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
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