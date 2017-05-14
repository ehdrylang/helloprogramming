from django.views.generic import ListView, DetailView
from django.shortcuts import render
from board.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'board/post_all.html'
    context_object_name = 'posts' #Default : object_list
    paginate_by = 2 #임시지정
    queryset = Post.objects.all() #Default : Model.objects.all()

    #count 구하는 함수 템플릿에서 {{count}}로 사용중
    def get_context_data(self,**kwargs):
        context = super(PostLV,self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

class PostDV(DetailView):
    model = Post
    date_field = 'modify_date' # 최근 게시글 순
