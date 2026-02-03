from django.contrib import admin
from .models import Master, Post, Comment
# Register your models here.

# admin.site.register(Post)
# admin.site.register(Master)
# admin.site.register(Comment)

class CommentInline(admin.TabularInline): # 혹은 StackedInline
    model = Comment
    extra = 1 # 기본으로 보여줄 빈 댓글 칸 수

@admin.register(Master)
class BoardMasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active') # 목록에 보여줄 필드
    prepopulated_fields = {'slug': ('name',)}    # 이름을 쓰면 슬러그 자동 생성

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'master', 'author', 'created_at') # 목록 설정
    list_filter = ('master', 'created_at')                     # 우측 필터 바
    search_fields = ('title', 'content')                      # 검색 창 추가
    raw_id_fields = ('author',)                               # 작성자 선택을 팝업으로 변경    
    inlines = [CommentInline] # 게시글 화면에 댓글 입력란 포함    
