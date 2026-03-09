from .models import Menu

def menu_context(request):
    # 모든 메뉴를 가져와서 템플릿에 전달
    menus = Menu.objects.filter(display_flag=True, use_flag=True).order_by('order_no')
    return {'menus': menus}