from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu
from common.models import Code

# Register your models here.
# admin.site.register(Menu)

# URL 유형에 해당하는 CodeType의 ID (예시)
URL_TYPE_CODE_ID = 1

@admin.register(Menu)
class MenuAdmin(MPTTModelAdmin):
    list_display = (
        "name",
        "parent",
        "lft",
        "rght",
        "tree_id",
        "level",
        "url_type",
        "url",
        "view",
        "order_no",
        "display_flag",
        "use_flag",
    )
    list_filter = ("display_flag", "use_flag", "url_type")
    search_fields = ("name", "url", "view")

    # db_field: 필드 객체, request: 현재 요청 객체
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "url_type":  # 필터링할 필드 이름 확인
            # 특정 조건(예: code가 'A'로 시작하는 것만)에 맞는 QuerySet 설정
            kwargs["queryset"] = Code.objects.filter(code_type_id=URL_TYPE_CODE_ID)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)