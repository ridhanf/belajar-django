from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'blog',
        'kontributor':'Ridhan Fafa',
    }
    return render(request,'blog/index.html',context)

def news(request):
    context = {
        'judul':'news',
        'kontributor':'Terra',
    }
    return render(request,'blog/index.html',context)

def story(request):
    context = {
        'judul':'story',
        'kontributor':'Sandra Bulog',
    }
    return render(request,'blog/index.html',context)
