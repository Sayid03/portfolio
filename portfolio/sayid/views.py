from django.shortcuts import render


def index(request):
    context = {
        'title': 'Sayid',
    }

    return render(request, 'sayid/index.html', context)
