from django.shortcuts import render


def index(request):
    context = {
        'judul': 'kelas terbuka',
        'kontributor': 'Ridhan',
    }
    return render(request, 'index.html', context)
