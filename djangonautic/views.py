# from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'abouts.html')
    

