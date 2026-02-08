from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    # path('', views.board_list, name='board_list'),
    path('<slug:master_slug>/', views.board_list, name='board_list_filter'),
    path('<slug:master_slug>/new/', views.board_write, name='board_write'),
    path('<slug:master_slug>/<int:pk>/', views.board_detail, name='board_detail'),
]
