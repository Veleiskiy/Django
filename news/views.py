from django.shortcuts import render, redirect
from .models import News, Comment
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
def index(request):
    news = News.objects.all()
    title = "Главная страница"
    return render(request, 'news/blog_list.html', {"news": news, "title": title})

def detail(request, pk):
    posts = News.objects.all()
    post = posts.get(pk=pk)
    title = post.title

    first = posts.first().id
    last = posts.last().id
    count = str(request.GET.get("post"))
    comments = Comment.objects.filter(news=post)

    if count == "prev":
        if post.id == first:
            return redirect("news:blog_detail", pk=last)
        prev_post = posts.filter(id__lt=post.id).last()
        return redirect("news:blog_detail", pk=prev_post.id)

    if count == "next":
        if post.id == last:
            return redirect("news:blog_detail", pk=first)
        next_post = posts.filter(id__gt=post.id).first()
        return redirect("news:blog_detail", pk=next_post.id)

    return render(request, 'news/blog_detail.html', {"news": post, "title": title, "comments": comments})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Загружает профиль instance, созданный сигналом
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'form': form})