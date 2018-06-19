from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, UserProfile
from .forms import PostForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
            username = request.GET['username']
            password = request.GET['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
            _user = User.objects.get(username=username)
            messages.success(request, 'Zalogowałeś się pomyślnie!')
            return render(request, 'blog/film_list.html', {'posts': posts, 'userAdd': _user})

def user_logout(request, user):
            logout(request)
            u = User.objects.get(id=1)
            zm, created = UserProfile.objects.get_or_create(user = u)
            zm.last_login_date_last = u.last_login
            zm.save()
            # _user.userprofile.login_date_last = _user.last_login
            # print (_user.userprofile.login_date_last)
            # _user.save()       
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
            return render(request, 'blog/film_list.html', {'posts': posts})



def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 
    return render(request, 'blog/film_list.html', {'posts': posts})

def post_all(request):
    posts = Post.objects.order_by('-published_date') 
    return render(request, 'blog/film_list.html', {'posts': posts})

def post_unpublish(request):
    posts = Post.objects.filter(published_date__lte!=timezone.now()).order_by('-published_date')
    return render(request, 'blog/film_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/film_detail.html', {'post': post})

def contact(request):
    return render(request, 'blog/contact.html')

def post_list_category(request, category):
    posts = Post.objects.filter(category=category).order_by('-published_date')
    return render(request, 'blog/film_list.html', {'posts': posts})

def post_list_author(request, author):
    posts = Post.objects.filter(author=author).order_by('-published_date')
    return render(request, 'blog/film_list.html', {'posts': posts})

def post_list_search(request):
    query = request.GET['q']
    posts = Post.objects.filter(title__contains=query).order_by('-published_date')
    return render(request, 'blog/film_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/film_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/film_edit.html', {'form': form})

def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/film_list.html', {'posts': posts})

def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish();
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/film_list.html', {'posts': posts})