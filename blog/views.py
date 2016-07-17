# from django.shortcuts import render


# Create your views here.


#
# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

from blog.models import Post
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post