from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', views.board_list, name='board_list'),
    # path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
