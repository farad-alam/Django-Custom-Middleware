from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print("home view caled")
    context = {"author":"Farad"}
    return TemplateResponse(request, 'blog/home.html', context)

def exception_view(request):
    print('this is exception view')
    a =10/0
    return HttpResponse('this from exception view')

