from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
import markdown
import pygments
from comments.forms import CommentForm

from blog.models import Post, Category, Tag


def index(request):
    # 直接在model中通过定义Meta来排序，所以在取出数据的时候就可以不用再排序了
    # post_list = Post.objects.all().order_by('-created_time')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    # post =  Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    # post_list = Post.objects.filter(category=cate).order_by('-created_time')
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    tag_item = get_object_or_404(Tag, pk=pk)
    post_list = tag_item.post_set.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
