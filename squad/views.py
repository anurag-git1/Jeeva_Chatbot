from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict)
    # return HttpResponse("Hello, world. You're at the squad index.")