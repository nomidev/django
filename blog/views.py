from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_at__isnull=True).order_by('-published_at')
    return render(request, 'post_list.html', {'posts': posts})