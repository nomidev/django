from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator 

from .models import Master, Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def board_list(request, master_slug=None):
    # 마스터 slug에 따라 게시물 필터링
    masters = Master.objects.filter(is_active=True)
    selected_master = None

    page = request.GET.get('page', 1)
    
    if master_slug:
        selected_master = get_object_or_404(Master, slug=master_slug, is_active=True)
        posts = Post.objects.filter(master=selected_master).select_related('author', 'master').order_by('-created_at')
        paginator = Paginator(posts, 10)  # 페이지당 10개 게시물
        page_post = paginator.get_page(page)
    else:
        # 모든 활성 마스터의 게시물
        posts = Post.objects.select_related('author', 'master').order_by('-created_at')[:20]
    
    return render(request, 'boards/board_list.html', {
        'posts': page_post,
        'masters': masters,
        'selected_master': selected_master,
    })


def board_detail(request, master_slug, pk):
    # 마스터 슬러그로부터 마스터 객체 조회
    master = get_object_or_404(Master, slug=master_slug, is_active=True)

    str1 = request.GET.get('master')
    print("master:", str1)

    # 상세 보기 예시: 게시물과 해당 댓글들 조회
    post = get_object_or_404(Post.objects.select_related('author', 'master'), pk=pk, master=master)
    comments = post.comments.select_related('author').all()

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('boards:board_detail', master_slug=master.slug, pk=post.pk)
    else:
        commentForm = CommentForm()
    
    return render(request, 'boards/board_detail.html', {'post': post, 'comments': comments, 'commentForm': commentForm, 'master': master})


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
            return redirect('boards:board_detail', master_slug=master.slug, pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'boards/board_form.html', {'form': form, 'master': master})


@login_required
def board_edit(request, master_slug, pk):
    # 마스터 슬러그로부터 마스터 객체 조회
    master = get_object_or_404(Master, slug=master_slug, is_active=True)
    
    # 게시물 조회
    post = get_object_or_404(Post, pk=pk, master=master)
    
    # 작성자만 수정 가능
    if post.author != request.user:
        return redirect('boards:board_detail', master_slug=master.slug, pk=post.pk)
    
    # 게시물 수정 뷰: GET -> 폼 표시, POST -> 저장
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('boards:board_detail', master_slug=master.slug, pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'boards/board_form.html', {'form': form, 'master': master, 'post': post})

"""
@login_required 와 @require_POST 를 같이 쓰게 되면
비로그인상태로 접근 -> 로그인 창 -> 로그인성공 - > 405 에러
redirect(request.GET.get('next')) 을 통해서 GET 방식으로 되돌아가기 때문에 생기는 로직상의 에러
@login_require 대신 request.user.is_authenticated 사용하
"""

# @login_required
@require_POST
def board_delete(request, master_slug, pk):
    if request.user.is_authenticated :
    # 마스터 슬러그로부터 마스터 객체 조회
        master = get_object_or_404(Master, slug=master_slug, is_active=True)
        
        # 게시물 조회
        post = get_object_or_404(Post, master=master, pk=pk)
        
        # 작성자만 삭제 가능
        if post.author == request.user:
            post.delete()
    
    return redirect('boards:board_list_filter', master_slug=master.slug)