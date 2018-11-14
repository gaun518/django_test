from django.shortcuts import render


def index(request):
    """/ トップページ"""
    context = {
        'name':'Yosuke',
    }
    return render(request, 'myapp/index.html', context)


def about(request):
    """/about アバウトページ"""
    return render(request, 'myapp/about.html')


def info(request):
    """/info インフォページ"""
    return render(request, 'myapp/info.html')
