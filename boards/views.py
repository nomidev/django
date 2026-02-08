from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Master, Post, Comment
from .forms import PostForm


# Create your views here.
def board_list(request, master_slug=None):
    # 마스터 slug에 따라 게시물 필터링
    masters = Master.objects.filter(is_active=True)
    selected_master = None
    
    if master_slug:
        selected_master = get_object_or_404(Master, slug=master_slug, is_active=True)
        posts = Post.objects.filter(master=selected_master).select_related('author', 'master').order_by('-created_at')
    else:
        # 모든 활성 마스터의 게시물
        posts = Post.objects.select_related('author', 'master').order_by('-created_at')[:20]
    
    return render(request, 'boards/board_list.html', {
        'posts': posts,
        'masters': masters,
        'selected_master': selected_master,
    })


def board_detail(request, master_slug, pk):
    # 마스터 슬러그로부터 마스터 객체 조회
    master = get_object_or_404(Master, slug=master_slug, is_active=True)

    # 상세 보기 예시: 게시물과 해당 댓글들 조회
    post = get_object_or_404(Post.objects.select_related('author', 'master'), pk=pk, master=master)
    comments = post.comments.select_related('author').all()
    return render(request, 'boards/board_detail.html', {'post': post, 'comments': comments})


@login_required
def board_write(request, master_slug):
    # 마스터 슬러그로부터 마스터 객체 조회
    master = get_object_or_404(Master, slug=master_slug, is_active=True)
    
    # 게시물 작성 뷰: GET -> 폼 표시, POST -> 저장
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.master = master  # 마스터 자동 설정
            post.save()
            return redirect('boards:board_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'boards/board_form.html', {'form': form, 'master': master})
