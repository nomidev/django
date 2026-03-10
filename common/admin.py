from django.contrib import admin
from .models import Codetype, Code

# Register your models here.
admin.site.register(Codetype)
# admin.site.register(Code)


@admin.register(Code)
class PostAdmin(admin.ModelAdmin):
    list_display = ('code_type', 'code', 'code_name', 'code_description') # 목록 설정
    list_filter = ('code_type',)                     # 우측 필터 바
    search_fields = ('code', 'code_name')                      # 검색 창 추가
    raw_id_fields = ('code_type',)                               # 코드 타입 선택을 팝업으로 변경    