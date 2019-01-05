from django.shortcuts import render
from core.models import Post

def home(request):
	return render(request, 'core/index.html')

def lista(request):
	lista = Post.objects.all().order_by('-id')
	return render(request,'core/lista.html',{'lista_post': lista})
