from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'info_app/index.html')

def show_info(request):
    return render(request, 'info_app/info.html')