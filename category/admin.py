from django.contrib import admin
from .models import Menu
from common.models import Code

# Register your models here.
# admin.site.register(Menu)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # db_field: 필드 객체, request: 현재 요청 객체
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "url_type":  # 필터링할 필드 이름 확인
            # 특정 조건(예: code가 'A'로 시작하는 것만)에 맞는 QuerySet 설정
            kwargs["queryset"] = Code.objects.filter(code_type_id=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)