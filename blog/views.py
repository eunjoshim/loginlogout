from django.shortcuts import render
from .models import Blog
from .form import BlogPost 

from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def blogpost(request):
    # 입력된 내용을 처리하는 기능 -> POST
    # 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
        else:
            form = BlogPost()
            return render(request, 'new.html',{'form':form})