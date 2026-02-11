from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', views.board_list, name='board_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
