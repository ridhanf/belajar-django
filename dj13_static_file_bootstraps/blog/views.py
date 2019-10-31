from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'Blog',
    'subjudul':'Blog kelas Terbuka',
  }
  return render(request,'index.html',context)