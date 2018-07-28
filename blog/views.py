from django.shortcuts import render

def index(request):
    # index.html을 출력
    return render(request, 'blog/index.html', {})

