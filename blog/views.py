from django.shortcuts import render

# Create your views here.

def home(request):
    print("home view caled")
    return render(request, 'blog/home.html')