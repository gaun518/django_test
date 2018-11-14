from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day


def index(request):
    context = {
        # DBに保存されているDayをすべて取り出すという処理、それを day_list という名前で day_list.html に渡している。
        'day_list':Day.objects.all(),
    }
    return render(request, 'diary/day_list.html', context)


def add(request):

    # 送信内容があれば DayCreateForm に紐付ける。POSTじゃなければ、空のフォーム
    form = DayCreateForm(request.POST or None)

    # method=POST、つまり送信ボタン押下時 form.is_valid で内容をチェックし、駄目ならFalseとなる。
    if request.method == 'POST' and form.is_valid():
        form.save()
        # POSTが成功したらリダイレクトさせる。2重投稿を防ぐ意味もある。
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html', context)


def update(request,pk):
    # pk は primarykey のこと

    # url の pk を基に Day を取得
    day = get_object_or_404(Day, pk = pk)

    # フォームに、取得した Day を紐付ける
    form = DayCreateForm(request.POST or None, instance = day)

    # method = POST つまり、送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html', context)


def delete(request,pk):
    # pk は primarykey のこと

    # url の pk を基に Day を取得
    day = get_object_or_404(Day, pk = pk)

    # method = POST つまり、送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day':day,
    }
    return render(request, 'diary/day_confirm_delete.html', context)


def detail(request,pk):
    # pk は primarykey のこと

    # url の pk を基に Day を取得
    day = get_object_or_404(Day, pk = pk)

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day':day,
    }
    return render(request, 'diary/day_detail.html', context)
