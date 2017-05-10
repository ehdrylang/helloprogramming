from django.views.generic import ListView, DetailView
from django.shortcuts import render
from board.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'board/post_all.html'
    context_object_name = 'posts'
    paginate_by = 12

class PostDV(DetailView):
    model = Post
    date_field = 'modify_date' # 최근 게시글 순
