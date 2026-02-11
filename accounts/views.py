from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST
import datetime
from boards.models import Master

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    today = datetime.date.today()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return render(request, 'accounts/login_success.html', {'user': user})
            return redirect(request.GET.get('next') or 'index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'today': today})

@require_POST
def logout_view(request):    
    logout(request)
    return redirect('index')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    masters = Master.objects.filter(is_active=True)

    # 회원가입 뷰: GET -> 폼 표시, POST -> 저장
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form, 'masters': masters,})