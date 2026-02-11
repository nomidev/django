from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Master

# Create your views here.
def index(request):
    msg = 'My Message'
    masters = Master.objects.filter(is_active=True)
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'home/index.html', {'msg': msg, 'masters': masters})
