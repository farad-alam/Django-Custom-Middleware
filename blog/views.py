from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    print("home view caled")
    return render(request, 'blog/home.html')

def exception_view(request):
    print('this is exception view')
    a =10/0
    return HttpResponse('this from exception view')