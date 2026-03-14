from .models import Menu
from django.db.models import Q

def menu_context(request):
    # 모든 메뉴를 가져와서 템플릿에 전달
    menus = Menu.objects.filter(Q(lft=1) | Q(level=1), display_flag=True, use_flag=True).order_by('order_no')
    return {'menus': menus}