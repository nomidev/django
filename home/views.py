from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    msg = 'My Message'
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'home/index.html', {'msg': msg})