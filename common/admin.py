from django.contrib import admin
from .models import CodeType, Code

# Register your models here.
admin.site.register(CodeType)
# admin.site.register(Code)


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('code_type', 'code', 'code_name', 'code_description') # 목록 설정
    list_filter = ('code_type',)                     # 우측 필터 바
    search_fields = ('code', 'code_name', '')                      # 검색 창 추가
    # autocomplete_fields = ('code_type',)                               # 코드 타입 선택을 자동완성으로 변경
    # raw_id_fields = ('code_type',)                               # 코드 타입 선택을 팝업으로 변경    