from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Master, Post
from django.db.models import Prefetch

# Create your views here.
def index(request):
    msg = 'My Message'
    masters = Master.objects.filter(is_active=True)
    # return HttpResponse("Hello, world. You're at the home index.")

    # 1. 각 카테고리에 속한 게시물을 최신순으로 정렬하여 미리 가져오기
    # (주의: Prefetch 내에서 슬라이싱[:5]은 지원되지 않으므로 템플릿에서 처리합니다)
    prefetch = Prefetch(
        'posts', 
        queryset=Post.objects.order_by('-created_at'),
        to_attr='recent_posts'
    )
    
    categories = Master.objects.prefetch_related(prefetch).all()

    return render(request, 'home/index.html', {'msg': msg, 'categories': categories})
