from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<slug:master_slug>/', views.board_list, name='board_list_filter'),
    path('<slug:master_slug>/new/', views.board_write, name='board_write'),
    path('<slug:master_slug>/<int:pk>/edit/', views.board_edit, name='board_edit'),
    path('<slug:master_slug>/<int:pk>/delete/', views.board_delete, name='board_delete'),
    path('<slug:master_slug>/<int:pk>/', views.board_detail, name='board_detail'),
]
