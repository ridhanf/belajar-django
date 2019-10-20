from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'About',
    'subjudul':'Tentang kelas terbuka',
  }
  return render(request,'index.html',context)