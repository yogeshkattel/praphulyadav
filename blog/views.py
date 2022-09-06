from asyncio import constants

from users.models import contributors
from .models import Post, Comment,Subscriber, News, ScheduledNotice
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm, NewsForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    
)
from django.core.paginator import Paginator, EmptyPage


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    

    

    def get_queryset(self):
        try:
            keyword = self.request.GET['q']
        except:
            keyword = ''
        if (keyword != ''):
            object_list = self.model.objects.filter(
                Q(content__icontains=keyword) | Q(title__icontains=keyword)) and Q(is_published=True)
        else:
            object_list = self.model.objects.filter(is_published=True)
        return object_list


class FilterPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    # filter the posts by category slug fields get
    def get_queryset(self, *args, **kwargs):
        
        try:
            category = self.kwargs['category']
           

        except:
            category = ''
        if (category != ''):
            object_list = self.model.objects.filter(category=category,is_published=True)
        else:
            object_list = self.model.objects.filter(is_published=True)
        return object_list
    


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    # get the user who created the post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['author'] = self.object.author
        # check if the current user is subscribed to the user in many to many field
        if self.request.user.is_authenticated:
            context['is_subscribed'] = Subscriber.objects.filter(
                user=self.object.author, subscribers=self.request.user)

        # print(context['is_subscribed'])
        # if self.request.user.is_authenticated:
        #     context['is_subscribed'] = Subscriber.objects.filter(
        #         user=self.object.author, subscribers=self.request.user).exists()
        
        return context
    

   





class PostCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Post
    form_class = PostForm
    def test_func(self):
        contributor = contributors.objects.filter(user=self.request.user).exists()
        if self.request.user.is_staff or contributor:
            return True
        return False


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateNewsView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        contributor = contributors.objects.filter(user=self.request.user).exists()
        if self.request.user.is_staff or contributor:
            return True
        return False



    
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'video_link', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_staff or self.request.user == post.author or self.request.user.is_contributor:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user == post.author or self.request.user.is_contributor:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(request.POST)
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(author=user, post=post, text=text).save()
        messages.success(request, "Your comment has been added successfully.")
    else:
        return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)

# view for subscribing model
@login_required
def subscribe(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        user = User.objects.get(id=post.author.id)
        # get sibscroiber data or create new one
        subscriber = Subscriber.objects.filter(user=user, subscribers=request.user.id).first()
        if subscriber:
            subscriber.subscribers.remove(request.user.id)
            messages.success(request, "You have been unsubscribed successfully.")
        else:
            suser = Subscriber.objects.filter(user=user).exists()
            if suser:
                suser = Subscriber.objects.filter(user=user).first()
                subscriber = User.objects.get(id=request.user.id)
                suser.subscribers.add(subscriber)
                suser.save()
            else:
                subs = Subscriber(user=user)
                subs.save()
                subscriber = User.objects.get(id=request.user.id)
                subs.subscribers.add(user)
                subs.save()
                
            messages.success(request, "You have been subscribed successfully.")
   
        
        
    else:
        return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)

# view for news feed with data from news mdoel
def news_feed(request, page=1):
    news = News.objects.all()
    paginator = Paginator(news, 6)
    schedulenotice = ScheduledNotice.objects.all()
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_pages) 
    return render(request, 'blog/news.html', {'news': news, 'notice': schedulenotice})


class News(ListView):
    model = News
    template_name = 'blog/news.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['notice'] = ScheduledNotice.objects.all()
        
        context['videos'] = Post.objects.all().order_by('-date_posted')[:3]

        return context

